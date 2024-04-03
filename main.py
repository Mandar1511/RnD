from load_data import load_data
from initialize_deltaK import initialize_deltaK, drop_deltas
from create_delta1tok import create_delta_tables
from connection import connection, cursor
from algorithm import algorithm
from table_list import select_cols


# Make sure that order of tables in "from" is lexicographical.
# query = """
#     select * from customer, lineitem, nation, orders where
#     customer.c_custkey = orders.o_custkey and lineitem.l_orderkey = orders.o_orderkey
#     and lineitem.l_returnflag = 590239 and customer.c_nationkey = nation.n_nationkey"""
select_cols = tuple(select_cols)
select_cols_str = ",".join(select_cols)
query = "SELECT * from department,employee where yob=selection_year and employee.dept_id = department.dept_id"
query2 = query.replace("*", select_cols_str)

user_input = input("Do you want to load the data? y/n\n")
if user_input == "y" or user_input == "Y":
    load_data(connection, cursor)

user_input = input("Do you want to create tables Δ1....Δk? y/n\n")
if user_input == "y" or user_input == "Y":
    create_delta_tables(connection, cursor)

user_input = input("Do you want to populate Δk ? y/n\n")
if user_input == "y" or user_input == "Y":
    initialize_deltaK(connection, cursor, query)

cursor.execute(query2)
possible_list = cursor.fetchall()
for row in possible_list:
    print(row)
    drop_deltas(connection, cursor)
    create_delta_tables(connection, cursor)
    curr_query = query
    curr_query += f" AND ({', '.join(select_cols)}) = ({row})"
    print(curr_query)
    initialize_deltaK(connection, cursor, curr_query)

    if algorithm(connection, cursor) == True:
        print("inserted")
    else:
        print("not inserted")
