import sqlite3
from dotenv import load_dotenv
import os

dbName = os.getenv('DBNAME')
tableName = 'laptopy'


class dbSql:
    def __init__(self, tableName: str):
        self.conn = sqlite3.connect(dbName)
        self.c = self.conn.cursor()
        self.tableName = tableName
        print(f'Connected database {dbName}')

    def createTable(self, dataType: dict):
        self.c.execute(f''' CREATE TABLE IF NOT EXISTS {self.tableName}(id INTEGER PRIMARY KEY AUTOINCREMENT)''')
        self.conn.commit()
        tabInfo = self.c.execute(f'PRAGMA table_info ({self.tableName})')\
            .fetchall()
        cols = []
        for element in tabInfo:
            cols.append(element[1])

        for key in dataType:
            if key not in cols:
                self.c.execute(f'''ALTER TABLE {self.tableName}
                                                    ADD COLUMN {key} {dataType[key]}''')
                self.conn.commit()
                print(f'Created table: {self.tableName} and {key}')

    def insertRowData(self, dataValue: dict):
        dataPlaceholder = f'({",".join(dataValue.keys())})'
        valuePlaceholder = f'({",".join("?" * len(dataValue))})'
        sql = f'''INSERT INTO {self.tableName}{dataPlaceholder}
                    VALUES{valuePlaceholder}'''
        val = (tuple(dataValue.values()))
        self.c.execute(sql, val)
        self.conn.commit()
        print(f'Insert value {tuple(dataValue.values())} to {self.tableName}')

    def info(self):
        sql = f'PRAGMA table_info ({self.tableName})'
        print(self.c.execute(sql).fetchall())

    def __del__(self):
        self.conn.close()
        print('Close connection')

