from flask import jsonify
from flask_restful import reqparse, Resource


class AllEntries(Resource):
    """Validates all entries on entry"""

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
