from flask import request
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from app.models.user_model import UserModel
from app.helpers.validator import Validate
parser = reqparse.RequestParser()


class Signup(Resource, UserModel):
    def post(self):
        parser.add_argument('email', required=True, type=str,
                            help=Validate.message('required', 'Email'))
        parser.add_argument(
            'username', required=True, type=str, help=Validate.message('required', 'Username'))
        parser.add_argument(
            'password', required=True, type=str, help=Validate.message('required', 'Password'))
        args = parser.parse_args()
        if not Validate.is_email(args.get('email')):
            return {
                "status": "FAILED",
                "message": "Wrong email format"
            }, 400

        if len(args.get('username')) < 5:
            return {
                "status": "FAILED",
                "message": "Username should have minimum 6 characters"
            }, 400

        if len(args.get('password')) < 5:
            return {
                "status": "FAILED",
                "message": "password should have minimum 6 characters"
            }, 400

        user = UserModel.save(args)
        if type(user) == str:
            return {
                "status": "FAILED",
                "message": user
            }, 409

        access_token = create_access_token(identity=user['username'])

        return {
            "status": "SUCCESS",
            "user": {
                "username": args.get('username'),
                "email": user["email"],
                "id": user["id"],
            },
            "token": access_token,
            "message": "Signup successfully"
        }, 201
