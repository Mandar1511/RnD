from table_list import tables, num_of_cols_per_table, primary_keys, primary_key_columns
import sys


def initialize_k_hashmaps(k, cursor):
    """
    This function initializes a hashmap for every Δ_i.
    each hashmap is of following format:
    hashed_row : set_of_tuples
    """
    # print("called")
    arr_of_maps = [dict() for x in range(k)]
    for i in range(0, k):
        query = f"select * from delta_{i+1}"
        try:
            cursor.execute(query)
            res = cursor.fetchall()
            for row in res:
                n = len(row)
                for j in range(n):
                    # row[j] is the key for i^th hashmap
                    adj = []
                    if row[j] not in arr_of_maps[i]:
                        arr_of_maps[i][row[j]] = set()
                    for l in range(n):
                        if j != l:
                            # add all columns to the tuple except the jth
                            adj.append(row[l])
                    arr_of_maps[i][row[j]].add(tuple(adj))
        except:
            sys.exit(f"Failed to fetch data from delta_{i+1}")
    # print("done")
    return arr_of_maps


is_T_inserted = False


def algorithm(connection, cursor):
    k = len(tables)
    global is_T_inserted
    is_T_inserted = False
    arr_of_maps = initialize_k_hashmaps(k, cursor)
    for i in range(len(tables)):
        primary_key = ",".join(primary_keys[i])
        table = tables[i]
        query = f"SELECT {primary_key} FROM {table} ORDER BY {primary_key}"
        cursor.execute(query)
        res = cursor.fetchall()  # this will store all primary keys in sorted order
        res = [
            tuple("'" + str(value) + "'" for value in item) for item in res
        ]  # Convert integers to strings for all rows
        # print("res")
        for j in range(len(res)):
            # print(j)
            # Now you are in one block
            primary_key_vals = ",".join(res[j])
            query = (
                f"SELECT * from {table} where ({primary_key}) = ({primary_key_vals})"
            )
            cursor.execute(query)
            block = cursor.fetchall()  # one block B
            hash_block = []
            for row in block:
                row_to_str = tuple(str(val) for val in row)
                hash_str = table
                hash_str = hash_str + "#" + "#".join(row_to_str) + "#"
                hash_block.append(hash_str)
            satistfied = 0
            # print(hash_block)
            # print(arr_of_maps[0])
            for x in range(len(hash_block)):
                if hash_block[x] in arr_of_maps[0]:
                    satistfied += 1
            # print(satistfied, hash_block)
            # print(arr_of_maps)
            if satistfied == len(hash_block):
                # print("True")
                return True

            connections_list = []
            block_is_useLess = False
            for l in range(len(hash_block)):
                if block_is_useLess:
                    break
                bi = hash_block[l]
                flag = 0
                for m in range(k):
                    if bi in arr_of_maps[m]:
                        connections_list.append(arr_of_maps[m][bi])
                        flag = 1
                if not flag:
                    block_is_useLess = True
            if block_is_useLess:
                continue
            st = set()
            # print("recurse")
            recurse(
                0, st, len(connections_list), connections_list, k, cursor, connection
            )
            # print("recurse-done")

    if not is_T_inserted:
        # print("False")
        return False
    else:
        return algorithm(connection, cursor)


def recurse(ind, st, n, connections_list, k, cursor, connection):
    # print("hi")
    # print(connections_list)
    if ind == n:
        union = set()
        for tup in st:
            for ele in tup:
                union.add(ele)
        union = sorted(union)
        str_to_insert = list(union)
        str_to_insert = ",".join(str_to_insert)
        if len(union) <= k and len(union) > 0:
            query = f"INSERT INTO delta_{len(union)} VALUES ('{str_to_insert}')"
            try:
                global is_T_inserted
                cursor.execute(query)
                connection.commit()
                # print("hi")
                is_T_inserted = True
            except Exception as e:
                connection.rollback()
        return
    current_set = list(connections_list[ind])
    for j in range(len(current_set)):
        st.add(current_set[j])
        recurse(ind + 1, st, n, connections_list, k, cursor, connection)
        st.discard(current_set[j])
