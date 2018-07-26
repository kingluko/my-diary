from flask import jsonify
from flask_restful import reqparse, Resource


class AllEntries(Resource):
    """Adds an Entry and gets a list of all entries"""
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument(
            'title', required=True, trim=True,
            help='Provide a valid title')
        self.reqparse.add_argument(
            'story', required=True, trim=True,
            help='Please enter a valid story')

    def post(self):
        """Add an Entry"""
        results = self.reqparse.parse_args()
        title = results.get('title')
        story = results.get('story')



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
