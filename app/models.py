from datetime import datetime
from passlib.hash import sha256_crypt
from app import DbConnection

db = DbConnection()


class Users:
    """Class for creating users"""
    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        self.password = sha256_crypt.encrypt(str(password))

    def signup_user(self):
        db.query("""INSERT INTO users(name, username, email, password)
        VALUES({}, {}, {}, {})""".format(
            self.name, self.username, self.email, self.password))

        return "Registration Successful"

    def signin_user(self):
        result = db.query(
            """SELECT * FROM users WHERE username = %s""", self.username)
        if result > 0:
            data = db.fetchone
            print(data)


class Entries:
    pass
