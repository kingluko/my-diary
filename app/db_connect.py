import psycopg2


class DbConnect:

    def __init__(self):
        try:
            # Create connection using psycopg2
            self.connect = psycopg2.connect(
                "dbname=diary user=kitika password=spongebob host=localhost")
            # activates the connection cursor
            self.connect.autocommit = True
            self.cursor = self.connect.cursor()
        except psycopg2.DatabaseError as error:
            print(error)

    # def read_table(self, table_nme):
    #     self.connect.cursor.execute(f"SELECT * FRPM {table_name}")

    # def insert (self, **params):
    #     name = params.get("name")

    #     self.connect.cursor.execute(f"SELECT * FRPM {table_name}")



    # def create_users_table(self):
    #     table_users = (
    #         """
            # CREATE TABLE users(
            #     ID SERIAL PRIMARY KEY,
            #     FIRSTNAME VARCHAR(100) NOT NULL,
            #     LASTNAME VARCHAR(100) NOT NULL,
            #     EMAIL VARCHAR(100) UNIQUE NOT NULL,
            #     PASSWORD VARCHAR(100) NOT NULL
            # )
    #         """
    #     )
    #     self.cursor.execute(table_users)

    # def create_entries_table(self):
    #     table_entries = (
    #         """
    #         CREATE TABLE entries(
    #             ID SERIAL PRIMARY KEY,
    #             DATE VARCHAR(100) NOT NULL
    #             TITLE VARCHAR NOT NULL,
    #             STORY VARCHAR NOT NULL
    #         )
    #         """
    #     )
    #     self.cursor.execute(table_entries)
