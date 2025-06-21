#logout.py
from flask import request, session
from flask_restful import Resource
from extensions import db
from models import User

class Logout(Resource):
    def delete(self):
        if 'user_id' in session:
            session.pop('user_id')
            return {}, 204
        return {'error': 'Unauthorized'}, 401