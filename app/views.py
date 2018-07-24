from flask import Flask, jsonify, request
import json
from app.models import Entries


entries_data = []


app = Flask(__name__)


@app.route('/api/v1/entries', methods=['GET'])
def fetch_all_entries():
    return jsonify(entries_data), 200


@app.route('/api/v1/entries/<int:id>', methods=['GET'])
def get_one_entry(id):
    for entry in entries_data:
        if entry['id'] == id:
            return jsonify(entry), 200
        else:
            return jsonify({'message': 'Entry not found'})


@app.route('/api/v1/entries', methods=['POST'])
def create_entry():
    request_data = request.get_json()
    new_entry = {
        'id': request_data['id'],
        'title': request_data['title'],
        'story': request_data['story']
    }
    for entry in entries_data:
        if request_data['id'] == entry['id']:
            return jsonify({'message': 'Entry already exists'}), 400
    entries_data.append(new_entry)
    return jsonify({'message': "Entry Added"}), 201


@app.route('/api/v1/entries/<int:id>', methods=['PUT'])
def update_entry(id):
    for entry in entries_data:
        if entry['id'] == id:
                request_data = request.get_json()
                new_entry = {'title': request_data['title'], 'story': request_data['story']}
                entry.update(new_entry)
                return jsonify({'message': "Entry modified successfully"}), 200


@app.route('/api/v1/entries/<int:id>', methods=['DELETE'])
def delete_entry(id):
    for entry in entries_data:
        if entry['id'] == id:
            entries_data.remove(entry)
            return jsonify({'message': "Entry deleted successfully"})
    return jsonify({'message': 'Entry not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
