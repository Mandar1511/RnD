import psycopg2
import sys


def db_connection(database, host, user, password, port):
    try:
        conn = psycopg2.connect(
            database=database,
            host=host,
            user=user,
            password=password,
            port=port,
        )
        return conn
    except:
        sys.exit("Failed to connect to the database")
