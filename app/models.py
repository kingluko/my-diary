import datetime


class User:
    def __init__(self, firstname, lastname, email, password):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
    

class Entries():
    """This method initializes the entry"""
    def __init__(self, title, story, date_created, user_id):
        self.id = 0
        self.title = title
        self.date_created = date_created
        self.story = story
        self.user_id = user_id  
