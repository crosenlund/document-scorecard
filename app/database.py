import psycopg2
import logging


# connect to the database and return a cursor object to manipulate the database
def connect_to_db():
    # Connect to an existing database
    try:
        conn = psycopg2.connect("dbname=postgres user=postgres password=postgres port=5433")
    except:
        logging.info("unable to connect to the requested database, please review and try again")
        exit()

    try:
        # Open a cursor to perform database operations
        return conn.cursor(), conn
    except:
        logging.info("Unable to create a cursor for the database")
        exit()


# Make the changes to the database persistent
def commit(conn):

    try:
        conn.commit()
        # logging.info("Commit successful")
    except:
        logging.info("Unable to commit to the database")
        exit()


# Close communication with the database
def close(cur, conn):
    try:
        cur.close()
        conn.close()
        # logging.info("Close successful")
    except:
        logging.info("Unable to close communication to the database")
        exit()
