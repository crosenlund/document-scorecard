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

    if existing_field(id):
        cur.execute("DELETE FROM fields WHERE id = '" + id + "';")
        cur.execute("DELETE FROM fields_in_groups WHERE field_id = '" + id + "';")

    commit(conn)
    close(cur, conn)


# edit a field's info
def edit_field(id, name, score, data, not_equal):

    cur, conn = connect_to_db()

    cur.execute("UPDATE field SET "
                "name = '" + name + "', "
                "score = '" + score + "', "
                "data = '" + data + "',"
                "not_equal = '" + not_equal + "'"
                " where id = " + id + ";")

    commit(conn)
    close(cur, conn)


# see if a field exists in the database
def existing_field(id):
    cur, conn = connect_to_db()

    if id:
        cur.execute("SELECT * FROM fields where id = '" + id + "';")
    else:
        logging.info("id was sent to this method (fields.existing_fields")
        return False

    row = cur.fetchone()

    close(cur, conn)
    # return true if a row in the database equals the id passed to this function, else false
    return row != None


