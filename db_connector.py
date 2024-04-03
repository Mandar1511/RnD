import psycopg2
import sys


def db_connector():
    try:
        # connection = psycopg2.connect(
        #     dbname="tpch", user="postgres", password="1234", host="localhost", port=5432
        # )
        connection = psycopg2.connect(
            dbname="test",
            user="postgres",
            password="1234",
            host="localhost",
            port=5432,
        )

        cursor = connection.cursor()
        return connection, cursor
    except psycopg2.Error as e:
        sys.exit("Failed to connect to the database: " + str(e))
