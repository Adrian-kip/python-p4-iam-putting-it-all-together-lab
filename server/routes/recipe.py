#recipe.py
from flask import request, session
from flask_restful import Resource
from extensions import db
from models import User

class RecipeIndex(Resource):
    def get(self):
        if 'user_id' not in session:
            return {'error': 'Unauthorized'}, 401
            
        recipes = Recipe.query.all()
        return [recipe.to_dict() for recipe in recipes], 200

    def post(self):
        if 'user_id' not in session:
            return {'error': 'Unauthorized'}, 401
            
        data = request.get_json()
        try:
            new_recipe = Recipe(
                title=data['title'],
                instructions=data['instructions'],
                minutes_to_complete=data['minutes_to_complete'],
                user_id=session['user_id']
            )
            db.session.add(new_recipe)
            db.session.commit()
            
            return new_recipe.to_dict(), 201
            
        except ValueError as e:
            return {'errors': [str(e)]}, 422
        except Exception as e:
            return {'errors': [str(e)]}, 422