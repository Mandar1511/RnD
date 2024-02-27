from db_connection import db_connection
from table_list import tables, num_of_cols_per_table

connection = db_connection("tpch", "localhost", "postgres", "1234", 5432)
cursor = connection.cursor()


k = len(tables)

try:
    # create tables from delta_1 ... delta_k. where delta_i contains i columns with text datatype
    for i in range(1, k + 1):
        table_name = f"delta_{i}"
        columns = ", ".join([f"column{j} text" for j in range(1, i + 1)])
        create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
        cursor.execute(create_table_query)
        print(f"Table '{table_name}' created successfully.")
    connection.commit()
except KeyError as e:
    print("Error creating tables:", e)

# Make sure that order of tables in from is lexicographical.
query = """
    select * from customer, lineitem, nation, orders where 
    customer.c_custkey = orders.o_custkey and lineitem.l_orderkey = orders.o_orderkey 
    and lineitem.l_returnflag = 590239 and customer.c_nationkey = nation.n_nationkey"""
cursor.execute(query)
res = cursor.fetchall()

for ind in range(len(res)):
    row = res[ind]
    delta_columns = []
    jstart = 0
    for i in range(len(num_of_cols_per_table)):
        hash_str = f"{tables[i]}#"
        for j in range(jstart, jstart + num_of_cols_per_table[i]):
            hash_str = hash_str + str(row[j]) + "#"
        delta_columns.append(hash_str)
        jstart += num_of_cols_per_table[i]
    delta_row_values = ", ".join(
        f"'" + delta_columns[i] + "'" for i in range(0, len(delta_columns))
    )
    populate_delta_query = f"INSERT INTO delta_{k} VALUES ({delta_row_values})"
    cursor.execute(populate_delta_query)
    connection.commit()

print(res)
connection.close()
cursor.close()
