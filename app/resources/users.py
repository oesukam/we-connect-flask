from flask import request
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from app.models.user_model import UserModel
from app.helpers.validator import Validate


class Signup(Resource, UserModel):
    def post(self):
        parser = reqparse.RequestParser()
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

        if not args.get('username') or len(args.get('username')) < 5:
            return {
                "status": "FAILED",
                "message": "Username should have minimum 6 characters"
            }, 400

        if not args.get('password') or len(args.get('password')) < 5:
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


class Login(Resource, UserModel):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            'username', required=True, type=str, help=Validate.message('required', 'Username'))
        parser.add_argument(
            'password', required=True, type=str, help=Validate.message('required', 'Password'))
        args = parser.parse_args()

        if args.get('username') and len(args.get('username')) < 5:
            return {
                "status": "FAILED",
                "message": "Username should have minimum 6 characters"
            }, 400

        if not args.get('password') or len(args.get('password')) < 5:
            return {
                "status": "FAILED",
                "message": "password should have minimum 6 characters"
            }, 400

        user = UserModel.find_by_username(args.get('username'))
        if not user:
            return {
                "status": "FAILED",
                "message": "Username and password don't match"
            }, 401

        access_token = create_access_token(identity=user['username'])

        return {
            "status": "SUCCESS",
            "user": {
                "username": args.get('username'),
                "email": user["email"],
                "id": user["id"],
            },
            "token": access_token
        }, 200
