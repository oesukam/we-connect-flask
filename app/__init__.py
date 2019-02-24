"""Initial Module"""
from flask import Flask
from flask_restful import Api
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)

from app.resources.users import Signup
from app.models.user_model import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and UserModel.verify_hash(password, user["password"]):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)


def create_app():
    """App init method"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret@secret'
    jwt = JWTManager(app)
    api = Api(app, prefix='/api')

    api.add_resource(Signup, '/auth/register')
    return app
