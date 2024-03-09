from load_data import load_data
from initialize_deltaK import initialize_deltaK
from create_delta1tok import create_delta_tables
from connection import connection, cursor

query = """
    select * from customer, lineitem, nation, orders where 
    customer.c_custkey = orders.o_custkey and lineitem.l_orderkey = orders.o_orderkey 
    and lineitem.l_returnflag = 590239 and customer.c_nationkey = nation.n_nationkey"""

user_input = input("Do you want to load the data? y/n\n")
if user_input == "y" or user_input == "Y":
    load_data(connection, cursor)

user_input = input("Do you want to create tables Δ1....Δk? y/n\n")
if user_input == "y" or user_input == "Y":
    create_delta_tables(connection, cursor)

user_input = input("Do you want to populate Δk ? y/n\n")
if user_input == "y" or user_input == "Y":
    initialize_deltaK(connection, cursor, query)
