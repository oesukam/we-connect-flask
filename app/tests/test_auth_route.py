import json
from unittest import TestCase
from app import create_app

app = create_app()


class TestLogin(TestCase):
    def test_login_without_data(self):
        with app.test_client() as client:
            res = client.post('/api/auth/login')
            self.assertEqual(res.status_code, 400)

    def test_login_with_fake_data(self):
        with app.test_client() as client:
            reqBody = {
                "username": "usernane",
                "password": "password"
            }
            res = client.post('/api/auth/login',
                              data=json.dumps(reqBody),
                              headers={'Content-Type': 'application/json'}
                              )

        data = json.loads(res.data.decode())

        self.assertEqual(res.status_code, 401)
        self.assertEqual(data['status'], 'FAILED')
        self.assertEqual(data['message'], "Username and password don't match")


class TestRegister(TestCase):
    def test_register_without_data(self):
        with app.test_client() as client:
            res = client.post('/api/auth/register')
            self.assertEqual(res.status_code, 400)

    def test_register_without_email(self):
        with app.test_client() as client:
            reqBody = {
                "username": "user",
                "password": "password"
            }
            res = client.post('/api/auth/register',
                              data=json.dumps(reqBody),
                              headers={'Content-Type': 'application/json'}
                              )

        data = json.loads(res.data.decode())

        self.assertEqual(res.status_code, 400)
        self.assertEqual(
            data['message']["email"], "Email is required")

    def test_register_with_wrong_username(self):
        with app.test_client() as client:
            reqBody = {
                "email": "email@email.com",
                "username": "user",
                "password": "password"
            }
            res = client.post('/api/auth/register',
                              data=json.dumps(reqBody),
                              headers={'Content-Type': 'application/json'}
                              )

        data = json.loads(res.data.decode())

        self.assertEqual(res.status_code, 400)
        self.assertEqual(data['status'], 'FAILED')
        self.assertEqual(
            data['message'], "Username should have minimum 6 characters")

    def test_register_success(self):
        with app.test_client() as client:
            reqBody = {
                "email": "email@email.com",
                "username": "username",
                "password": "password"
            }
            res = client.post('/api/auth/register',
                              data=json.dumps(reqBody),
                              headers={'Content-Type': 'application/json'}
                              )

        data = json.loads(res.data.decode())

        self.assertEqual(res.status_code, 201)
        self.assertEqual(data['status'], 'SUCCESS')
        # self.assertIsNotNone((data['status'])
        self.assertEqual(
            data['message'], "Signup successfully")
