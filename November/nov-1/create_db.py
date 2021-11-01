import sqlite3

connection = sqlite3.connect('database_schema.db')

cursor = connection.cursor()

with open('my_customers_schema.sql') as sql_file:
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)

connection.commit()