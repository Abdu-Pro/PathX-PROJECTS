import sqlite3

CREATE_FIELDS_TABLE = "CREATE TABLE fields (id INTEGER PRIMARY KEY, field_name TEXT, desription TEXT, salary INTEGER);"

INSERT_FIELDS = "INSERT INTO fields (field_name, description, salary) VALUES (?, ?, ?);"

GET_ALL_FIELDS = "SELECT * FROM fields;"
GET_FIENDS_BY_NAME = "SELECT * FROM fields WHERE field_name = ?;"

def connect():
    return sqlite3.connect(data.db)

def create_tables(connection):
    with connection:
        connection.excute(CREATE_FIELDS_TABLE)


def add_fields(connection, field_name, description, salary):
    with connection:
        connection.excute(INSERT_FIELDS, (field_name, description, salary))

def get_all_fields(connection):
    with connection:
        