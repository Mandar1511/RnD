from db_connection import db_connection

connection = db_connection("tpch", "localhost", "postgres", "1234", 5432)
cursor = connection.cursor()


tables = ["customer", "orders", "lineitem", "nation"]
num_of_cols_per_table = [9, 10, 17, 5]

columns = ", ".join([f"{table}_col text" for table in tables])

create_delta_query = f"CREATE TABLE IF NOT EXISTS delta ({columns})"
cursor.execute(create_delta_query)
connection.commit()

query = "select customer.1,'#' from customer, orders, lineitem, nation where customer.c_custkey = orders.o_custkey and lineitem.l_orderkey = orders.o_orderkey and lineitem.l_returnflag = 590239 and customer.c_nationkey = nation.n_nationkey"
cursor.execute(query)
res = cursor.fetchall()

for ind in range(len(res)):
    row = res[ind]
    delta_columns = []
    jstart = 0
    for i in range(len(num_of_cols_per_table)):  # 0->3
        hash_str = "#"
        for j in range(jstart, jstart + num_of_cols_per_table[i]):
            hash_str = hash_str + str(row[j]) + "#"
        delta_columns.append(hash_str)
        jstart += num_of_cols_per_table[i]
    delta_row_values = ", ".join(
        "'" + delta_columns[i] + "'" for i in range(0, len(delta_columns))
    )
    populate_delta_query = f"INSERT INTO delta VALUES ({delta_row_values})"
    cursor.execute(populate_delta_query)
    connection.commit()


connection.close()
cursor.close()
