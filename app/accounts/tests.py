from django.test import TestCase
from django.contrib.auth import get_user_model, authenticate
from django.test import TestCase
from rest_framework_simplejwt.tokens import RefreshToken

# User = get_user_model()

# class AuthTestCase(TestCase):
#     def setUp(self):
#         # Tạo user test
#         self.username = 'vanhveo'
#         self.password = '230823'
#         User.objects.create_user(username=self.username, password=self.password)

#     def test_authenticate_user(self):
#         user = authenticate(username=self.username, password=self.password)
#         self.assertIsNotNone(user)
#         self.assertEqual(user.username, self.username)

class TokenTestCase(TestCase):
    def setUp(self):
        self.refresh_token_str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTc0NTkzNDA2OSwiaWF0IjoxNzQ1ODQ3NjY5LCJqdGkiOiI3NjI5ODdiMWZlMDM0Yzg3OWE0NDlkOTRjZjMyMjgyYiIsInVzZXJfaWQiOjF9.8LJ4daqbF0ZYGbimjFZsIgoeNShcGHAWMhyvKsQqRCE"

    def test_access_token_from_refresh(self):
        try:
            refresh = RefreshToken(self.refresh_token_str)
            access_token = str(refresh.access_token)

            self.assertIsNotNone(access_token)
            print("Access Token:", access_token)
        except Exception as e:
            self.fail(f"Failed to create access token: {e}")
