from table_list import tables, num_of_cols_per_table


def initialize_deltaK(connection, cursor, query):
    k = len(tables)
    try:
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
            # print(delta_row_values)
            try:
                populate_delta_query = (
                    f"INSERT INTO delta_{k} VALUES ({delta_row_values})"
                )
                cursor.execute(populate_delta_query)
                connection.commit()
            except:
                print(f"Failed to insert {delta_row_values}")
                return
    except:
        print(f"Failed to fetch execute {query}")
        return
