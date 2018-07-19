from flask import Flask, jsonify, request
import json
from app.models import Entries


entries_data = [{
        'id' : 1,
        'title': 'Some interesting title',
        'story': 'Some very interesitng story'
        },{ 
        'id' : 2,
        'title': 'Some interesting title',
        'story': 'Some very interesitng story'
        },{
        'id' : 3,
        'title': 'Some interesting title',
        'story': 'Some very interesitng story'
        }]



app = Flask(__name__)

@app.route('/api/v1/entries', methods= ['GET'])
def fetch_all_entries():
    return jsonify(entries_data), 200

@app.route('/api/v1/entries/<int:id>', methods = ['GET'])
def get_one_entry():
    for entry in entries_data:
        if entry['id'] == id:
            return entry, 200
        else:
            return jsonify({'message': 'Entry not found'})

@app.route('/api/v1/entries', methods =['POST'])
def create_entry():
    request_data = request.get_json()      
    new_entry = {
        'id': id,
        'title': request_data['title'],
        'story': request_data['story']
    }
    entries_data.append(new_entry)    
    return {'message' : "Entry Added", 'entries': jsonify(entries_data)}, 201

@app.route('/api/v1/entries/<int:id>', methods = ['PUT'])
def update_entry():
    for entry in entries_data:
        if id == entry['id']:            
                request_data = request.get_json()
                update_entry = {
                    'title': request_data['title'],
                    'story': request_data['story']
                      }
                entry['title'] = update_entry['title']
                entry['story'] = update_entry['story']
                return {'message' : "The entry has been modified successfully", 'entry': entry}, 200    
    

if __name__ == '__main__':
    app.run(debug=True)