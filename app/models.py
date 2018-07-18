import datetime


class User:
    def __init__(self, id, firstname, lastname, email, password):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
    

class Entries():
    def __init__(self, id, title, story, user_id):
        self.id = id
        self.title = title
        self.date_created = datetime.datetime.now()
        self.story = story
        self.user_id = user_id  
