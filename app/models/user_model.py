"""User Model module"""

import uuid
from passlib.hash import pbkdf2_sha256 as sha256
USERS = []


class UserModel:
    """ User Model class with helper methods """

    def __init__(self, first_name='', last_name='', username='', email='', password=''):
        self._id = uuid.uuid4()
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.email = email

    def __str__(self):
        """Overwrite the string method"""
        return "id: {id}, username: {username}, email: {email}, first_name: {first_name}"

    @staticmethod
    def generate_hash(password):
        return sha256.hash(password)

    @staticmethod
    def verify_hash(password, hash):
        return sha256.verify(password, hash)

    @staticmethod
    def save(new_user):
        """ Add a new user by id """
        if not new_user:
            raise ValueError("Please provide user's information")
        for user in USERS:
            if user['username'] == new_user['username']:
                return 'Username already exists'
            if user['email'] == new_user['email']:
                return 'Email already exists'

        new_user["id"] = str(uuid.uuid4())
        new_user["password"] = sha256.hash(new_user["password"])
        USERS.append(new_user)
        return new_user

    @staticmethod
    def find_by_id(_id):
        """ Find a single user by id """
        if not _id:
            raise ValueError('Please provide the id')
        for user in USERS:
            if user['id'] == _id:
                return user
        return None

    @staticmethod
    def find_by_username(username):
        """ Find a single user by username """
        if not username:
            raise ValueError('Please provide the username')
        for user in USERS:
            if user['username'] == username:
                return user
        return None

    @staticmethod
    def remove_by_id(_id=''):
        """ Remove a user by id """
        if not _id:
            raise ValueError('Please provide the id')
        for key, user in enumerate(USERS):
            if user['id'] == _id:
                USERS.remove(key)
            return user
        return None

    @staticmethod
    def get_all():
        """ get all users """
        all_users = []
        for user in USERS:
            all_users.append(
                {
                    "id": user['id'],
                    "first_name": user["first_name"],
                    "last_name": user["last_name"],
                    "email": user["email"],
                    "username": user["username"]
                })
        return all_users
