from app import create_app
from flask import Flask
app = Flask(__name__)


"""
This file handles the logic for the different endpoints
"""

@app.route('/signin', methods=['POST', 'GET'])
def signin():
    pass

@app.route('/signup', methods=['POST'])
def signup():
    pass


@app.route('/entries', methods=['GET'])
def get_entries():
    pass

@app.route('entries/<int:id>', methods=['GET'])
def get_one_entry(id):
    pass

@app.route('entries', methods=['POST'])
def create_entry():
    pass

@app.route('entries/<int:id>', methods=['PUT'])
def modify_entry(id):
    pass