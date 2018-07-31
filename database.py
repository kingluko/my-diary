from app import DbConnection

db = DbConnection()


def create_tables():
    tables = (
        """
        CREATE TABLE IF NOT EXIST users(id serial PRIMARY KEY, name VARCHAR(100), email VARCHAR(100), username VARCHAR(30), password VARCHAR(100))
        """,
        """
        CREATE TABLE IF NOT EXIST entries(entry_id serial, user_id INTEGER REFERENCES users(id), title VARCHAR(200), story TEXT, date_created TIMESTAMP DEFAULT NOW()
        """
    )
    for table in tables:
        db.query(table)

if __name__ == '__main__':
    create_tables()
    