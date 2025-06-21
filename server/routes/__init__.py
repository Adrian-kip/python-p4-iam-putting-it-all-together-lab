from .signup import Signup
from .check_session import CheckSession
from .login import Login
from .logout import Logout
from .recipe import RecipeIndex

def initialize_routes(api):
    api.add_resource(Signup, '/signup')
    api.add_resource(CheckSession, '/check_session')
    api.add_resource(Login, '/login')
    api.add_resource(Logout, '/logout')
    api.add_resource(RecipeIndex, '/recipes')