#check_session.py
from flask import request, session
from flask_restful import Resource
from extensions import db
from models import User

class CheckSession(Resource):
    def get(self):
        user_id = session.get('user_id')
        if not user_id:
            return {'error': 'Unauthorized'}, 401
            
        user = User.query.filter(User.id == user_id).first()
        if not user:
            return {'error': 'Unauthorized'}, 401
            
        return user.to_dict(), 200