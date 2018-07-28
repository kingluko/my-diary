from flask import jsonify, request
from flask_restful import reqparse, Resource
from app.models import Users, Entries
from app import DbConnection
import json
from resources.decorator import is_logged_in

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
                'message': 'Entries found', 'entry': Entries.make_dict(entry)}
        else:
            return {'message': 'Entries not found'}
        db.close()      


class SingleEntry(Resource):
    @is_logged_in
    def put(self, user_id, entry_id):
        """Edit an Entry"""
        entry = Entries.get(user_id=user_id, entry_id=entry_id)
        if not entry:
            return {'message': 'The entry does not exist'}, 404
        else:
            results = request.get_json()
            new_title = results['title']
            new_story = results['story']

            db.query(
                "UPDATE entries SET title=%s, story=%s WHERE entry_id=%s",
                (new_title, new_story, entry_id))
            return{'message': 'Entry Updated'}, 201

    @is_logged_in
    def get(self, user_id, entry_id):
        """This method gets a single entry"""
        entry = Entries.get(user_id=user_id, entry_id=entry_id)
        if entry:
            return {
                'message': 'Entry found', 'entry': Entries.make_dict(entry)}
        else:
            return {'message': 'Entry not found'}, 404
        db.close()

    @is_logged_in
    def delete(self, user_id, entry_id):
        """This method is used to delte an entry"""
        entry = Entries.get(user_id=user_id, entry_id=entry_id)
        if not entry:
            return {'message': 'Entry not found'}, 404
        else:
            db.query(
                "DELETE FROM entries WHERE entry_id=%s", (str(entry_id))
            )
            return {'message': 'Entry has been deleted successfully'}, 201
