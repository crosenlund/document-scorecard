import json
import logging
import sys
import time
from app import database
from app import groups
from lxml import etree

from app import fields


# use test_database.py method connect_to_db()
def connect_to_db():
    return database.connect_to_db()


# use test_database.py method commit()
def commit(conn):
    database.commit(conn)


# use test_database.py method commit()
def close(cur, conn):
    database.close(cur, conn)


# add a new field to a specified scenario
def add_field(scen_id, name, score, data, not_equal):
    cur, conn = connect_to_db()
    field_id = -1

    if existing_scenario(scen_id, None):
        field_id = fields.create_field(cur, name, score, data, not_equal)

        cur.execute(
            "INSERT INTO fields_in_groups (scenario_id, group_id, field_id) VALUES (%s, %s, %s);"
            , (scen_id, None, field_id))

    else:
        logging.info("The selected scenario does not exists (id = " + scen_id + ")")

    commit(conn)
    close(cur, conn)

    if field_id is not -1:
        logging.info("successfully added scenario '" + name + "' (id = " + str(scen_id) + ", " +
                     " " + name + ", " + score + "," + data + "," +
                     " " + not_equal + ")")

    return field_id


# add a new group to the database
def add_group(scen_id, name, qualifier, qualifier_field):
    cur, conn = connect_to_db()
    new_id = -1
    if existing_scenario(scen_id, None):
        new_id = groups.create_group(cur, name, qualifier, qualifier_field)

        if not groups.existing_group(new_id):
            cur.execute(
                "INSERT INTO groups_in_groups (scenario_id, parent_group_id, child_group_id) VALUES (%s, %s, %s);"
                , (scen_id, None, new_id))
        else:
            logging.info(
                "There was an issue adding a group (id = " + str(new_id) + ") to a scenario (id = " + str(
                    scen_id) + ").")
    else:
        logging.info("There was an issue adding to scenario (id = " + str(scen_id) + ").")

    commit(conn)
    close(cur, conn)

    if 'new_id' is not -1:
        logging.info("successfully added group '" + name + "' (id = " + str(new_id) + ", " +
                     " " + name + ", " + qualifier + "," + qualifier_field + ")")

    return new_id


# add a new scenario to the database
def add_scenario(name, description, doc_type, fulfillment_type, schema_name, root_name):
    scen_id = -1
    if name:
        cur, conn = connect_to_db()

        if existing_scenario(None, name):
            logging.info("A scenario with the name '" + name + "' already exists.")
        else:
            cur.execute(
                "INSERT INTO scenarios (name, description, doc_type, fulfillment_type, "
                "schema_name, root_name, date_created, date_modified) VALUES (%s, %s, %s, %s, %s, %s, CURRENT_TIMESTAMP(2), CURRENT_TIMESTAMP(2)) RETURNING id;",
                (name, description, doc_type, fulfillment_type, schema_name, root_name))
            scen_id = cur.fetchone()[0]

        commit(conn)
        close(cur, conn)

        if scen_id is not -1:
            logging.info("successfully added scenario '" + name + "' (id = " + str(scen_id) + ", " +
                         " " + name + ", " + description + "," + doc_type + "," +
                         " " + fulfillment_type + "," + schema_name + ", " + root_name + ")")

    else:
        logging.info("name cannot be null or empty string")

    return scen_id


# delete a scenario from the database
def delete_scenario(id):
    cur, conn = connect_to_db()
    deleted = False
    error = ''
    if existing_scenario(id, ""):
        cur.execute("DELETE FROM scenarios WHERE id = '" + str(id) + "';")
        logging.info("successfully deleted scenario (id = " + str(id) + ")")
        deleted = True
    else:
        logging.info("The selected scenario does not exists (id = " + str(id) + ")")
        error = "The selected scenario does not exists (id = " + str(id) + ")"

    commit(conn)
    close(cur, conn)

    return deleted, error


# create a new scenario by copying an existing one
def copy_scenario(id, name):
    error = ''
    copy = True
    if name:
        cur, conn = connect_to_db()

        if not existing_scenario(id, ""):
            logging.info("The selected scenario does not exist.")
            copy = False
            error += "The selected scenario does not exist."

        if existing_scenario("", name):
            logging.info("A scenario with the name '" + name + "' already exists.")
            copy = False
            error += "A scenario with the name '" + name + "' already exists."

        if copy:
            try:
                info, error = get_info(id)
                add_scenario(name, info[2], info[3], info[4], info[5], info[6])
                logging.info("successfully copied scenario '" + name + "' (id = " + str(id) + ", " +
                             " " + name + ", " + info[2] + ", " + info[3] + ", " +
                             " " + info[4] + ", " + info[5] + ", " + info[6] + ")")
            except:
                copy = False
                logging.info("Unexpected error: %r" % sys.exc_info()[0])
                error += ("Unexpected error: %r" % sys.exc_info()[0])

        commit(conn)
        close(cur, conn)

    else:
        logging.info("name cannot be null or empty string")
        error += "name cannot be null or empty string"

    return copy, error


# edit a scenario's info
def edit_scenario(id, name, description, doc_type, fulfillment_type, schema_name, root_name, same_name):
    if name:
        cur, conn = connect_to_db()
        update = True
        error = ''

        if not existing_scenario(id, ""):
            logging.info("The selected scenario does not exist.")
            update = False
            error += "The selected scenario does not exist."

        # checks if we are changing the name of the scenario and then checks that the name does not already exist
        if not same_name and existing_scenario("", name):
            logging.info("A scenario with the name '" + name + "' already exists.")
            update = False
            error += "A scenario with the name '" + name + "' already exists."

        if update:
            edit_string = ''
            if name:
                edit_string += "name = '" + name + "', "
            if description:
                edit_string += "description = '" + description + "', "
            if doc_type:
                edit_string += "doc_type = '" + doc_type + "', "
            if fulfillment_type:
                edit_string += "fulfillment_type = '" + fulfillment_type + "', "
            if schema_name:
                edit_string += "schema_name = '" + schema_name + "', "
            if root_name:
                edit_string += "root_name = '" + root_name + "', "
            edit_string += "date_modified = DEFAULT"
            try:
                cur.execute("UPDATE scenarios SET " + edit_string + " where id = " + str(id) + ";")
                logging.info("successfully updated scenario '" + name + "' (id = " + str(id) + ", " +
                             " " + name + ", " + description + ", " + doc_type + ", " +
                             " " + fulfillment_type + ", " + schema_name + ", " + root_name + ")")
            except:
                logging.info("Unexpected error: %r" % sys.exc_info()[0])
                error += ("Unexpected error: %r" % sys.exc_info()[0])
                update = False

        commit(conn)
        close(cur, conn)

    else:
        logging.info("name cannot be null or empty string")
        return False, "name cannot be null or empty string"

    return update, error


# see if a scenario exists in the database
def existing_scenario(id, name):
    cur, conn = connect_to_db()
    if id and name:
        cur.execute("SELECT * FROM scenarios where id = '" + str(id) + "' or name = '" + name + "'")
    elif id:
        cur.execute("SELECT * FROM scenarios where id = '" + str(id) + "'")
    elif name:
        cur.execute("SELECT * FROM scenarios where name = '" + name + "'")
    else:
        logging.info("id nor name were sent to this method")
        return False

    row = cur.fetchone()

    close(cur, conn)
    # return true if a row in the database equals the name/id passed to this function, else false
    return row != None


# get a list of all the scenarios in the database
def get_all_scenarios():
    cur, conn = connect_to_db()

    cur.execute("SELECT * FROM scenarios")
    all_scenarios = cur.fetchall()

    scen_list = []
    scens = []
    for scenario in all_scenarios:
        scens.append(
            {"scenId": scenario[0], "name": scenario[1], "description": scenario[2], "doctype": scenario[3],
             "fulfillmenttype": scenario[4], "schema": scenario[5], "rootname": scenario[6],
             "datecreated": str(scenario[7]), "datemodified": str(scenario[8])})

    scen_list.append({"scenarios": scens})
    close(cur, conn)
    return scens


# return the id of a scenario when given the name
def get_id(name):
    cur, conn = connect_to_db()
    cur.execute("SELECT id FROM scenarios WHERE name = '" + name + "'")

    row = cur.fetchone()[0]

    return row

# get the scenarios info
def get_info(id):
    cur, conn = connect_to_db()
    error = ''
    if not existing_scenario(id, ""):
        logging.info("The selected scenario does not exist (id = " + str(id) + ".")
        error += "The selected scenario does not exist."
        row = None
    else:
        cur.execute("SELECT * FROM scenarios where id = '" + str(id) + "'")

        row = cur.fetchone()

    return row, error


# return a scenario as json, uses methods build_fields and build_fields
def to_xml(id):
    start_time = time.time()
    print("---to_xml started %s  ---" % start_time)

    cur, conn = connect_to_db()
    if existing_scenario(id, None):
        cur.execute("SELECT * FROM scenarios where id = '" + str(id) + "'")

        row = cur.fetchone()

        root_name = row[6]
        root_node = etree.Element(root_name)
        root_node = (build_fields_xml(cur, id, root_node, False))
        root_node = (build_groups_xml(cur, id, root_node, False))

        close(cur, conn)

    print("---to_xml finished in %s seconds ---" % (time.time() - start_time))
    if 'root_node' in locals():
        return etree.tostring(root_node, pretty_print=True), ''
    else:
        return [], 'Unable to retrieve the selected scenario. Please try again or report an issue.'


# return a scenario as json, uses methods build_fields and build_fields
def to_element_tree(id):
    start_time = time.time()
    print("---to_xml started %s  ---" % start_time)

    cur, conn = connect_to_db()
    if existing_scenario(id, None):
        cur.execute("SELECT * FROM scenarios where id = '" + str(id) + "'")

        row = cur.fetchone()

        root_name = row[6]
        root_node = etree.Element(root_name)
        root_node = (build_fields_xml(cur, id, root_node, False))
        root_node = (build_groups_xml(cur, id, root_node, False))

        close(cur, conn)

    print("---to_xml finished in %s seconds ---" % (time.time() - start_time))
    if 'etree' in locals():
        return etree, ''
    else:
        return [], 'Unable to retrieve the selected scenario. Please try again or report an issue.'


# helper method building the groups in XML for the scenario
def build_groups_xml(cur, id, add_to_group, group_fields):
    if group_fields:
        cur.execute("SELECT child_group_id FROM groups_in_groups where parent_group_id = '" + str(id) + "'")
    else:
        cur.execute("SELECT child_group_id FROM groups_in_groups where scenario_id = '" + str(id) + "'")

    groups_to_build = cur.fetchall()

    for group in groups_to_build:
        group_id = str(group[0])

        cur.execute(
            "SELECT * FROM groups WHERE id = '" + str(group_id) + "';")
        group_info = cur.fetchone()
        group_name = group_info[1]
        group_node = etree.Element(group_name)
        group_node = (build_fields_xml(cur, group_id, group_node, True))
        group_node = (build_groups_xml(cur, group_id, group_node, True))
        add_to_group.append(group_node)

    return add_to_group


# helper method building the fields in XML for the scenario
def build_fields_xml(cur, id, group, group_field):
    if group_field:
        cur.execute("SELECT field_id FROM fields_in_groups where group_id = '" + str(id) + "'")
    else:
        cur.execute("SELECT field_id FROM fields_in_groups where scenario_id = '" + str(id) + "'")

    fields_to_build = cur.fetchall()

    for field in fields_to_build:
        field_id = str(field[0])

        cur.execute(
            "SELECT * FROM fields WHERE id = '" + str(field_id) + "';")
        field_info = cur.fetchone()
        field_name = field_info[1]
        field_node = etree.Element(field_name)
        field_node.set('score', str(field_info[2]))
        field_node.text = field_info[3]
        if field_info[4]:
            field_node.set('not_equal', str(field_info[4]))
        group.append(field_node)
    return group


# return a scenario as json, uses methods build_fields and build_fields
def to_json(id):
    start_time = time.time()
    print("---to_json started %s  ---" % start_time)
    scen_list = []

    cur, conn = connect_to_db()
    if existing_scenario(id, None):
        cur.execute("SELECT * FROM scenarios where id = '" + str(id) + "'")

        row = cur.fetchone()

        fields_built = build_fields_json(cur, id, False)
        groups_built = build_groups_json(cur, id, False)
        if fields_built:
            if groups_built:
                scen_list.append(
                    {"scenId": id, "rootName": row[6], "groups": build_groups_json(cur, id, False),
                     "fields": build_fields_json(cur, id, False)})
            if not groups_built:
                scen_list.append(
                    {"scenId": id, "rootName": row[6], "fields": build_fields_json(cur, id, False)})

        if not fields_built:
            if groups_built:
                scen_list.append(
                    {"scenId": id, "rootName": row[6], "groups": build_groups_json(cur, id, False),
                     "fields": build_fields_json(cur, id, False)})
            if not groups_built:
                scen_list.append({"scenId": id, "rootName": row[6]})

        close(cur, conn)

    print("---to_json finished in %s seconds ---" % (time.time() - start_time))
    if 'row' in locals():
        # return json.dumps(scen_list), ''
        return scen_list, ''
    else:
        return [], 'Unable to retrieve the selected scenario. Please try again or report an issue.'


# helper method building the groups in json for the scenario
def build_groups_json(cur, id, group_fields):
    if group_fields:
        cur.execute("SELECT child_group_id FROM groups_in_groups where parent_group_id = '" + str(id) + "'")
    else:
        cur.execute("SELECT child_group_id FROM groups_in_groups where scenario_id = '" + str(id) + "'")

    groups_to_build = cur.fetchall()

    group_list = []

    for group in groups_to_build:
        group_id = str(group[0])

        build_fields_json(cur, id, True)
        cur.execute(
            "SELECT * FROM groups WHERE id = '" + str(group_id) + "';")
        group_info = cur.fetchone()
        fields_built = build_fields_json(cur, group_id, True)
        groups_built = build_groups_json(cur, group_id, True)
        if fields_built:
            if groups_built:
                group_list.append({"groupId": group_info[0], "name": group_info[1], "qualifier": group_info[2],
                                   "qualifier_field": group_info[3], "groups": groups_built,
                                   "fields": fields_built})
            if not groups_built:
                group_list.append({"groupId": group_info[0], "name": group_info[1], "qualifier": group_info[2],
                                   "qualifier_field": group_info[3], "fields": fields_built})

        if not fields_built:
            if groups_built:
                group_list.append({"groupId": group_info[0], "name": group_info[1], "qualifier": group_info[2],
                                   "qualifier_field": group_info[3], "groups": groups_built})
            if not groups_built:
                group_list.append({"groupId": group_info[0], "name": group_info[1], "qualifier": group_info[2],
                                   "qualifier_field": group_info[3]})

    return group_list


# helper method building the fields in json for the scenario
def build_fields_json(cur, id, group_field):
    if group_field:
        cur.execute("SELECT field_id FROM fields_in_groups where group_id = '" + str(id) + "'")
    else:
        cur.execute("SELECT field_id FROM fields_in_groups where scenario_id = '" + str(id) + "'")

    fields_to_build = cur.fetchall()

    field_list = []

    for field in fields_to_build:
        field_id = str(field[0])

        cur.execute(
            "SELECT * FROM fields WHERE id = '" + str(field_id) + "';")
        field_info = cur.fetchone()
        field_list.append(
            {"fieldId": field_info[0], "name": field_info[1], "score": field_info[2], "data": field_info[3],
             "not_equal": field_info[4]})

    return field_list
