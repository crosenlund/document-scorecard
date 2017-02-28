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
def add_field(group_id, name, score, data, not_equal, requires):

    cur, conn = connect_to_db()
    field_id = -1
    if existing_group(group_id):
        field_id = fields.create_field(cur, name, score, data, not_equal, requires)

        cur.execute(
            "INSERT INTO fields_in_groups (scenario_id, group_id, field_id) VALUES (%s, %s, %s);"
            , (None, group_id, field_id))

    else:
        logging.info("The selected group does not exist.")

    commit(conn)
    close(cur, conn)

    if 'new_id' is not -1:
        logging.info("successfully added field '%r' (id = %r, %r, %r, %r, %r, %r)" % (name, field_id, name, score, data, not_equal, requires))

    return field_id


# add a new group to the database
def add_group(group_id, name, qualifying_value, qualifying_field, requires_one):
    cur, conn = connect_to_db()
    new_id = -1
    error = ''
    if existing_group(group_id):
        new_id = create_group(cur, name, qualifying_value, qualifying_field, requires_one)

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
                     " " + name + ", " + qualifying_value + ", " + qualifying_field + ", " + requires_one + ")")

    return new_id


# create a new group
def create_group(cur, name, qualifying_value, qualifying_field, requires_one):
    cur.execute("INSERT INTO groups (name, qualifying_value, qualifying_field, requires_one) VALUES (%s, %s, %s, %s) RETURNING id",
                (name, qualifying_value, qualifying_field, requires_one))
    return cur.fetchone()[0]


# delete a group from the database
def delete_group(id):
    cur, conn = connect_to_db()
    success = False

    if existing_group(id):
        cur.execute("DELETE FROM groups WHERE id = '" + str(id) + "';")
        success = True
    else:
        logging.info("The selected group does not exist.")

    commit(conn)
    close(cur, conn)

    return success


# edit a group's info, make sure the group (by id) exists first
def edit_group(id, name, qualifying_value, qualifying_field, requires_one):
    cur, conn = connect_to_db()
    success = False

    if existing_group(id):
        cur.execute("UPDATE groups SET "
                    "name = '" + name + "', " +
                    "qualifying_value = '" + qualifying_value + "', " +
                    "qualifying_field = '" + qualifying_field + "', " +
                    "requires_one = '" + requires_one + "'" +
                    " where id = " + str(id) + ";")
        success = True
    else:
        logging.info("The selected group does not exist.")

    commit(conn)
    close(cur, conn)

    return success


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
