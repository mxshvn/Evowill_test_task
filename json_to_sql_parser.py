def create_table(self, json_data, table_name):
    data = json.loads(json_data)

    column_definitions = []
    for key, value in data.items():
        if isinstance(value, (int, float)):
            column_type = 'REAL'
        else:
            column_type = 'TEXT'
        column_definitions.append(f'{key} {column_type}')

    create_table_sql = (
        f'CREATE TABLE IF NOT EXISTS {table_name} '
        f'(id SERIAL PRIMARY KEY, {", ".join(column_definitions)});'
    )

    with self.conn.cursor() as cursor:
        cursor.execute(create_table_sql)
    self.conn.commit()