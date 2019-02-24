import unittest
import os
from app.models.user_model import UserModel
# import app.models.user_model.UserModel

print(os.path)


class TestUserModel(unittest.TestCase):
    """User model unit test"""

    def setUp(self):
        self.user_id = ""
        self.user_data = {
            "username": "username",
            "email": "username@email.com",
            "password": "123456"
        }

    def test_save_user(self):
        """Test saving a user"""

        user_model = UserModel()
        user = user_model.save(new_user=self.user_data)
        self.user_id = user["id"]
        self.assertEqual(user["username"], self.user_data["username"])
        self.assertEqual(user["email"], self.user_data["email"])
        self.assertIsNot(user["id"], None)

    def test_find_user_by_id(self):
        """Test saving a user"""
        print(self.user_id)
        user = UserModel.find_by_id(self.user_id)
        self.assertEqual(user["username"], self.user_data["username"])
        self.assertEqual(user["email"], self.user_data["email"])


if __name__ == '__main__':
    unittest.main()
