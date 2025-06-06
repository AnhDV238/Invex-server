from django.urls import path
from .views import LoginView
from .views import RefreshTokenView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('refresh-token/', RefreshTokenView.as_view())
]
