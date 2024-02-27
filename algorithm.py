from db_connection import db_connection
from table_list import tables, num_of_cols_per_table, primary_keys, primary_key_columns

connection = db_connection("tpch", "localhost", "postgres", "1234", 5432)
cursor = connection.cursor()

for i in range(len(tables)):
    primary_key = ",".join(primary_keys[i])
    table = tables[i]
    primary_key_column = primary_key_columns[i]
    num_columns = num_of_cols_per_table[i]
    query = f"SELECT * FROM {table} ORDER BY {primary_key}"
    cursor.execute(query)
    res = cursor.fetchall()
    blocks = []
    for k in range(len(res)):
        j = k
        block = []
        while j < len(res) and all(res[j][l] == res[k][l] for l in primary_key_column):
            block.append(res[j])
            j += 1
        blocks.append(block)
        print(len(block))
        k = j
