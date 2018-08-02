from flask import jsonify, request
from flask_restful import reqparse, Resource
from app.models import Users, Entries
from app import DbConnection
import json
from app.resources.decorator import is_logged_in

db = DbConnection()


class AllEntries(Resource):
    """Validates all entries on entry"""
    parser = reqparse.RequestParser()
    parser.add_argument(
        'title',
        required=True,
        type=str,
        trim=True,
        help='Enter a valid title')

    parser.add_argument(
        'story',
        required=True,
        type=str,
        trim=True,
        help='Enter a valid text')

    @is_logged_in
    def post(self, user_id):
        """"This method adds a story to the database"""
        results = AllEntries.parser.parse_args()
        title = results.get('title')
        story = results.get('story')
        # Adding post to database
        entry = Entries(title=title, user_id=user_id, story=story)
        entry.post()
        return {'message': 'Entry posted successfully'}, 201

    @is_logged_in
    def get(self, user_id, entry_id=None):
        """This method gets the entry for a given user"""
        entry = Entries.get(user_id=user_id)
        if entry:
            return {
                # displays the entries as dictionaries
                'message': 'Entries found', 'entry': Entries.make_dict(entry)}, 201
        else:
            return {'message': 'Entries not found'}, 404


class SingleEntry(Resource):
    @is_logged_in
    def put(self, user_id, entry_id):
        """This method is used to update an Entry"""
        entry = Entries.get(user_id=user_id, entry_id=entry_id)
        if not entry:
            # returns a message if the entry was not found
            return {'message': 'The entry does not exist'}, 404
        else:
            results = request.get_json()
            new_title = results['title']
            new_story = results['story']
            # Updates the entry stored in the db with new data
            db.query(
                "UPDATE entries SET title=%s, story=%s WHERE entry_id=%s",
                (new_title, new_story, entry_id))
            return{'message': 'Entry Updated'}, 200

    @is_logged_in
    def get(self, user_id, entry_id):
        """This method gets a single entry"""
        entry = Entries.get(user_id=user_id, entry_id=entry_id)
        if entry:
            return {
                'message': 'Entry found', 'entry': Entries.make_dict(entry)}
        else:
            return {'message': 'Entry not found'}, 404

    @is_logged_in
    def delete(self, user_id, entry_id):
        """This method is used to delte an entry"""
        entry = Entries.get(user_id=user_id, entry_id=entry_id)
        # if entry is not found returns error
        if not entry:
            return {'message': 'Entry not found'}, 404
        else:
            # deletes from db
            db.query(
                "DELETE FROM entries WHERE entry_id=%s", [entry_id]
            )
            return {'message': 'Entry has been deleted successfully'}, 200
