import sqlite3
import os


class DBWriter:
    def __init__(self, db_name=None, table_name=None):
        if not db_name:
            db_name = 'results.sqlite3'

        if not table_name:
            table_name = 'jobs'

        if os.path.exists(db_name):
            os.remove(db_name)

        self._connection = sqlite3.connect(db_name)
        self._cursor = self._connection.cursor()
        self._headers = None
        self._table_name = table_name

    def _create_table(self, headers):
        if self._headers is None:
            self._headers = headers
            columns = ',\n'.join(f'{column_name} text' for column_name in headers)

            sql = f'''
            CREATE TABLE IF NOT EXISTS {self._table_name} (
                {columns}
            );
            '''
            self._cursor.execute(sql)
            self._connection.commit()

    def write(self, item):
        if self._headers is None:
            self._create_table(item.keys())

        keys = ', '.join(f':{column_name}' for column_name in item)

        sql = f"INSERT INTO {self._table_name} VALUES ({keys})"
        self._cursor.execute(sql, item)
        self._connection.commit()

    def destruct(self):
        self._connection.commit()
        self._connection.close()
