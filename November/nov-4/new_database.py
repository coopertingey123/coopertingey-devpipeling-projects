import sqlite3

connection = sqlite3.connect('cars.db')

cursor = connection.cursor()

with open("new_schema.sql") as sql_file:
    sql_as_string = sql_file.read()
    cursor.executescript(sql_as_string)
connection.commit()    