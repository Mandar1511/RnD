from db_connector import db_connection
from table_list import tables, num_of_cols_per_table, primary_keys, primary_key_columns

connection = db_connection("tpch", "localhost", "postgres", "1234", 5432)
cursor = connection.cursor()

k = len(tables)
arr_of_maps = [{} for x in range(k)]  # initializing k hashmaps
for i in range(0, k):
    query = f"select * from delta_{i+1}"
    cursor.execute(query)
    res = cursor.fetchall()
    for row in res:
        n = len(row)
        for j in range(n):
            adj = []
            if row[j] not in arr_of_maps[i]:
                arr_of_maps[i][row[j]] = set()
            for l in range(n):
                if j != l:
                    adj.append(row[l])
            arr_of_maps[i][row[j]].add(tuple(adj))

for i in range(len(tables)):
    primary_key = ",".join(primary_keys[i])
    table = tables[i]
    primary_key_column = primary_key_columns[i]
    num_columns = num_of_cols_per_table[i]
    query = f"SELECT {primary_key} FROM {table} ORDER BY {primary_key}"
    cursor.execute(query)
    res = cursor.fetchall()  # this will store all primary keys in sorted order
    res = [
        tuple(str(value) for value in item) for item in res
    ]  # Convert integers to strings within tuples
    for j in range(len(res)):
        # Now you are in one block
        primary_key_vals = ",".join(res[j])
        query = f"SELECT * from {table} where ({primary_key_vals}) = {primary_key}"
        cursor.execute(query)
        block = cursor.fetchall()  # one block
        # print(block)
        hash_block = []
        for row in block:
            row_to_str = tuple(str(val) for val in row)
            hash_str = table
            hash_str = hash_str + "#" + "#".join(row_to_str) + "#"
            hash_block.append(hash_str)

        # Store delta before travelling in Block
        print(len(hash_block))
        connections_list = []
        block_is_useLess = False
        for l in range(len(hash_block)):
            if block_is_useLess:
                break
            bi = hash_block[l]
            for m in range(k):
                if bi in arr_of_maps[m]:
                    connections_list.append(arr_of_maps[m][bi])
                else:
                    block_is_useLess = True
        if block_is_useLess:
            continue
