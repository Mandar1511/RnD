from db_connection import db_connection
from load_data import load_data

connection = db_connection("tpch", "localhost", "postgres", "1234", 5432)
cursor = connection.cursor()

x = input("Do you want to load the data? y/n\n")
if x == "y":
    load_data(connection, cursor)
else:
    pass
connection.close()
cursor.close()
