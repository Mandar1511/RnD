from initialize_deltaK import initialize_deltaK, drop_deltas
from create_delta1tok import create_delta_tables
from connection import connection, cursor
from algorithm import algorithm
from table_list import select_cols


select_cols = tuple(select_cols)
select_cols_str = ",".join(select_cols)
query = "select * from lineitem"
query2 = f"select DISTINCT {select_cols_str} from lineitem"
cursor.execute(query2)
possible_list = cursor.fetchall()
for row in possible_list:
    row = [str(x) for x in row]
    drop_deltas(connection, cursor)
    create_delta_tables(connection, cursor)
    curr_query = query
    row = ",".join(row)
    if query2.find("WHERE") == -1:
        curr_query += f" WHERE ({', '.join(select_cols)}) = ({row})"
    else:
        curr_query += f" AND ({', '.join(select_cols)}) = ({row})"
    print(curr_query)
    initialize_deltaK(connection, cursor, curr_query)
    if algorithm(connection, cursor) == True:
        print(row)
    else:
        continue
