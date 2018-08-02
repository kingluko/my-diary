from datetime import datetime
from passlib.hash import sha256_crypt
from app import DbConnection
from flask import jsonify
import json

db = DbConnection()


class Users:
    """Class for creating users"""
    def __init__(self, name, username, email, password):
        self.name = name
        self.username = username
        self.email = email
        # encrypts the password to be stored as hash
        self.password = sha256_crypt.encrypt(str(password))

    def signup_user(self):
        db.query(
            # stores the instance for each user
            "INSERT INTO users(name, email, username, password) VALUES(%s, %s, %s, %s)",
            (self.name, self.email, self.username, self.password))


class Entries:
    # creates an instance for each story
    def __init__(self, user_id, title, story):
        self.user_id = user_id
        self.title = title
        self.story = story

    def post(self):
        """This method adds an entry into the database"""
        db.query(
            "INSERT INTO entries(user_id, title, story) VALUES(%s, %s, %s)",
            (self.user_id, self.title, self.story))

    @staticmethod
    def get(user_id, entry_id=None):
        """This method is used to get a single or all entries"""
        if entry_id:
            # gets a single entry once the entry_id value is true
            db.query(
                "SELECT * FROM entries WHERE user_id=%s AND entry_id=%s",
                (user_id, entry_id)
            )
            entries = db.cur.fetchall()
            return entries
        else:
            # gets all entries once the entry_id value is false
            db.query(
                "SELECT * FROM entries WHERE user_id = %s", [user_id]
            )
            entry = db.cur.fetchall()
            return entry

    @staticmethod
    # This method creates a list of entry dictionaries from the database
    def make_dict(entry_list):
        # cretes an empty list
        entries = []
        for entry in entry_list:
            # creates empty dictionary
            new_dict = {}
            # updates the dictionary with the entry details
            new_dict.update({
                'entry_id': entry[0],
                'title': entry[2],
                'story': entry[3],
                'date_created': entry[4].strftime("%A, %d %B, %Y")
                })
            # appends the list with entry dictionaries
            entries.append(new_dict)
        return entries

