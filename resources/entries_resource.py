from flask import jsonify
from flask_restful import reqparse, Resource
from app.models import Users, Entries


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

    def post(self):
        """Add an Entry"""
        results = AllEntries.parser.parse_args()
        title = results.get('title')
        story = results.get('story')

        #g flask
        # entry = (title=title, story=story)

    def get(self):
        """Fetch all Entries by user"""
        pass   


class SingleEntry(Resource):
    def put(self, id):
        """Edit an Entry"""
        pass

    def get(self, id):
        """Edit a single entry"""
        pass

    def delete(self, id):
        """Delete a single entry"""
        pass
