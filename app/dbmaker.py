import os
from psycopg2 import connect


def connect_db(configuration=None):
    if configuration == "testing":
        name_db = os.getenv('DATABASE_TEST')
    else:
        name_db = os.getenv('DATABASE_NAME')

    host = os.getenv("DATABASE_HOST")
    user_db = os.getenv("DATABASE_USERNAME")
    password_db = os.getenv("DATABASE_PASSWORD")

    conn_db = "host, name_db, user_db, password_db"
    return connect(conn_db)


if __name__ == '__main__':
    connect_db(os.getenv("APP_SETTINGS"))
