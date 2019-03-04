import unittest
import os
from app.models.user_model import UserModel
# import app.models.user_model.UserModel

print(os.path)


class TestUserModel(unittest.TestCase):
    """User model unit test"""

    def setUp(self):
        self.user_data = {
            "username": "username",
            "email": "username@email.com",
            "password": "123456"
        }

    def test_save_user(self):
        """Test saving a user"""
        UserModel.remove_by_username(username=self.user_data["username"])
        user = UserModel.save(new_user=self.user_data)
        print(user)
        self.assertEqual(user["username"], self.user_data["username"])
        self.assertEqual(user["email"], self.user_data["email"])
        self.assertIsNot(user["id"], None)

    def test_find_user_by_id(self):
        """Test saving a user"""
        UserModel.remove_by_username(self.user_data["username"])
        new_user = UserModel.save(new_user=self.user_data)
        user = UserModel.find_by_id(new_user['id'])
        self.assertEqual(user["username"], new_user["username"])
        self.assertEqual(user["email"], new_user["email"])


if __name__ == '__main__':
    unittest.main()
