from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from djangogamers.apps.authentication.views import RegistrationAPIView, LoginAPIView

urlpatterns = [
    path('users/', RegistrationAPIView.as_view(), name="register-user"),
    path('users/login/', LoginAPIView.as_view(), name="login-user"),
    path('users/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]