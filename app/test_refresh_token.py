from django.test import TestCase
from rest_framework_simplejwt.tokens import RefreshToken

class TokenTestCase(TestCase):
    def setUp(self):
        self.refresh_token_str = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzQ1ODUwODA2LCJpYXQiOjE3NDU4NTA3NzYsImp0aSI6IjViNzllMDFmOTUwNDRkYTBhYzE0YmM4OGNmMjU1ZGQ2IiwidXNlcl9pZCI6MX0.-KcjrRjWsG67Y-aDaJwY9AAWgt2RryaCbwzSe0kfDS0"

    def test_access_token_from_refresh(self):
        try:
            refresh = RefreshToken(self.refresh_token_str)
            access_token = str(refresh.access_token)

            self.assertIsNotNone(access_token)
            print("Access Token:", access_token)
        except Exception as e:
            self.fail(f"Failed to create access token: {e}")
