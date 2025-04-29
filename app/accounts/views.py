from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated

class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'detail': 'Username and password are required.'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)
        if user:
            refresh = RefreshToken.for_user(user)
            return Response({
                'status': '1',
                'response': {
                    'access': str(refresh.access_token),
                    'refresh': str(refresh)
                }
            }, status=status.HTTP_200_OK)

        return Response({
                'status': '2',
                'response': {
                    'message':'user not found'
                }
                })
    def get(self, request):
        permission_classes = [IsAuthenticated]
        user = request.user
        if not user.is_authenticated:
            return Response({
                'status': '2',
                'response': {
                    'message': 'token not work'
                }
            })
        return Response({
            'status': '1',
            'response': {"username": user.username}
        }, status=status.HTTP_200_OK)

class RefreshTokenView(APIView):
  def post(self, request):
    refresh_token = request.data.get('refresh')
    try:
      refresh = RefreshToken(refresh_token)
      access_token = refresh.access_token
      return Response({
        'status': '1',
        'response': {
          'access': str(access_token),
          'refresh': str(refresh),
        }
      }, status=status.HTTP_200_OK)
    except Exception as e:
      return Response({
        'status': '2',
        'response': {
          'message': 'Invalid or expired refresh token.',
        }
      }, status=status.HTTP_401_UNAUTHORIZED)
