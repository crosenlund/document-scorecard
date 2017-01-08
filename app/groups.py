import logging

from app import database

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


# add a new field a specified group
def add_field(group_id, name, score, data, not_equal):

    cur, conn = connect_to_db()
    field_id = -1
    if existing_group(group_id):
        field_id = fields.create_field(cur, name, score, data, not_equal)

        cur.execute(
            "INSERT INTO fields_in_groups (scenario_id, group_id, field_id) VALUES (%s, %s, %s);"
            , (None, group_id, field_id))

    else:
        logging.info("The selected group does not exist.")

    commit(conn)
    close(cur, conn)

    if 'new_id' is not -1:
        logging.info("successfully added field '" + name + "' (id = " + str(field_id) + ", " +
                     " " + name + ", " + score + ", " + data + ", " + not_equal + ")")

    return field_id


# add a new group to the database
def add_group(group_id, name, qualifier, qualifier_field):
    cur, conn = connect_to_db()
    new_id = -1
    error = ''
    if existing_group(group_id):
        new_id = create_group(cur, name, qualifier, qualifier_field)

        if not existing_group(new_id):
            cur.execute(
                "INSERT INTO groups_in_groups (scenario_id, parent_group_id, child_group_id) VALUES (%s, %s, %s);"
                , (None, group_id, new_id))
        else:
            logging.info(
                "There was an issue adding a group (id = " + str(new_id) + ") to a group (id = " + str(group_id) + ").")
            error += "There was an issue adding a group (id = " + str(new_id) + ") to a group (id = " + str(group_id) + ")."
    else:
        logging.info("There was an issue adding to group (id = " + str(group_id) + ").")
        error += "There was an issue adding to group (id = " + str(group_id) + ")."
    commit(conn)
    close(cur, conn)

    if 'new_id' is not -1:
        logging.info("successfully added group '" + name + "' (id = " + str(new_id) + ", " +
                     " " + name + ", " + qualifier + "," + qualifier_field + ")")

    return new_id


# create a new group
def create_group(cur, name, qualifier, qualifying_field):
    cur.execute("INSERT INTO groups (name, qualifier, qualifying_field) VALUES (%s, %s, %s) RETURNING id",
                (name, qualifier, qualifying_field))
    return cur.fetchone()[0]


# delete a group from the database
def delete_group(id):
    cur, conn = connect_to_db()

    if existing_group(id):
        cur.execute("DELETE FROM groups WHERE id = '" + id + "';")
    else:
        logging.info("The selected group does not exist.")

    commit(conn)
    close(cur, conn)


# edit a group's info, make sure the group (by id) exists first
def edit_group(id, name, qualifier, qualifying_field):
    cur, conn = connect_to_db()

    if existing_group(id):
        cur.execute("UPDATE groups SET "
                    "name = '" + name + "', " +
                    "qualifier = '" + qualifier + "', " +
                    "qualifying_field = '" + qualifying_field + "'" +
                    " where id = " + id + ";")
    else:
        logging.info("The selected group does not exist.")

    commit(conn)
    close(cur, conn)


# see if a group exists in the database
def existing_group(id):

    cur, conn = connect_to_db()
    if id:
        cur.execute("SELECT * FROM groups where id = '" + str(id) + "';")
    else:
        logging.info("ERROR: " + str(id) + " was sent to (groups.existing_group")
        return False

    row = cur.fetchone()
    close(cur, conn)
    # return true if a row in the database equals the id passed to this function, else false
    return row != None
