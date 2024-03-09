from table_list import tables


def create_delta_tables(connection, cursor):
    """
    creates tables from delta_1 ... delta_k. where delta_i contains i columns with text datatype
    """
    k = len(tables)
    try:
        for i in range(1, k + 1):
            table_name = f"delta_{i}"
            columns = ", ".join([f"column{j} text" for j in range(1, i + 1)])
            create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
            cursor.execute(create_table_query)
            connection.commit()
            print(f"Table '{table_name}' created successfully.")
    except KeyError as e:
        print("Error creating tables:", e)
