import csv
import sys


def load_data(connection, cursor):
    csvfile_to_tablename_mappings = {
        "./tpch_1/customer.csv": "customer",
        "./tpch_1/lineitem.csv": "lineitem",
        "./tpch_1/nation.csv": "nation",
        "./tpch_1/orders.csv": "orders",
        "./tpch_1/part.csv": "part",
        "./tpch_1/partsupp.csv": "partsupp",
        "./tpch_1/region.csv": "region",
        "./tpch_1/supplier.csv": "supplier",
    }

    for csv_file, table_name in csvfile_to_tablename_mappings.items():
        with open(csv_file, "r") as file:
            csv_reader = csv.reader(file)
            for row in csv_reader:
                try:
                    cursor.execute(
                        f"INSERT INTO {table_name} VALUES ({', '.join(['%s']*len(row))});",
                        row,
                    )
                    connection.commit()
                except:
                    sys.exit("Something went wrong while loading data from " + csv_file)
        print(csv_file + " successfully loaded")
