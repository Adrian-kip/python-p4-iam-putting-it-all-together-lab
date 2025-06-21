#signup.py
from flask import request, session
from flask_restful import Resource
from extensions import db
from models import User
from sqlalchemy.exc import IntegrityError


class Signup(Resource):
    def post(self):
        data = request.get_json()
        
        try:
            new_user = User(
                username=data['username'],
                image_url=data.get('image_url'),
                bio=data.get('bio')
            )
            new_user.password_hash = data['password']
            db.session.add(new_user)
            db.session.commit()
            
            session['user_id'] = new_user.id
            
            return new_user.to_dict(), 201
            
        except IntegrityError:
            return {'error': 'Username already exists'}, 422
        except ValueError as e:
            return {'error': str(e)}, 422
        except Exception as e:
            return {'error': str(e)}, 422