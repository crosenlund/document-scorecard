import logging

from app import database


# use test_database.py method connect_to_db()
def connect_to_db():
    return database.connect_to_db()


# use test_database.py method commit()
def commit(conn):
    database.commit(conn)


# use test_database.py method commit()
def close(cur, conn):
    database.close(cur, conn)


# create a new field
def create_field(cur, name, score, data, not_equal):
    if not not_equal:
        not_equal = False
    cur.execute("INSERT INTO fields (name, score, data, not_equal) VALUES (%s, %s, %s, %s) RETURNING id",
                (name, score, data, not_equal))
    return cur.fetchone()[0]


# delete a group from the database
def delete_field(id):
    cur, conn = connect_to_db()

    success = False
    if existing_field(id):
        cur.execute("DELETE FROM fields WHERE id = '" + str(id) + "';")
        cur.execute("DELETE FROM fields_in_groups WHERE field_id = '" + str(id) + "';")
        success = True

    commit(conn)
    close(cur, conn)

    return success



# edit a field's info
def edit_field(id, name, score, data, not_equal):

    cur, conn = connect_to_db()

    cur.execute("UPDATE fields SET "
                "name = %r, "
                "score = %r, "
                "data = %r,"
                "not_equal = %r"
                " where id = %r;" % (name, score, data, not_equal, id))

    commit(conn)
    close(cur, conn)

    return True


# see if a field exists in the database
def existing_field(id):
    cur, conn = connect_to_db()

    if id:
        cur.execute("SELECT * FROM fields where id = '" + str(id) + "';")
    else:
        logging.info("Unable to find a field, %s was sent to this method (fields.existing_fields" % str(id))
        return False

    row = cur.fetchone()

    close(cur, conn)
    # return true if a row in the database equals the id passed to this function, else false
    return row != None


