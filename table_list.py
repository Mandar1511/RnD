# input from user
# tables = [
#     "customer",
#     "lineitem",
#     "nation",
#     "orders",
# ]
# num_of_cols_per_table = [9, 10, 17, 5]

# primary_keys = [
#     ["c_custkey"],
#     ["l_orderkey", "l_linenumber"],
#     ["n_nationkey"],
#     ["o_orderkey"],
# ]

# primary_key_columns = [[0], [0, 3], [0], [0]]

tables = ["department", "employee"]
num_of_cols_per_table = [2, 4]
primary_keys = [["dept_id"], ["id"]]
primary_key_columns = [[0], [0]]
select_cols = ["id", "name", "yob"]
