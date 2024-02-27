# Take as input from user
tables = [
    "customer",
    "lineitem",
    "nation",
    "orders",
]
num_of_cols_per_table = [9, 10, 17, 5]

primary_keys = [
    ["c_custkey"],
    ["l_orderkey", "l_linenumber"],
    ["n_nationkey"],
    ["o_orderkey"],
]

primary_key_columns = [[0], [0, 3], [0], [0]]
