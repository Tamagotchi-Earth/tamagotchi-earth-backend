from django.urls import path
from dj_rest_auth.views import LoginView, LogoutView, PasswordChangeView, UserDetailsView
from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import RegisterView
from rest_framework_simplejwt.views import TokenVerifyView

# Manually select dj-rest-auth views
urlpatterns = [
    path('auth/login/', LoginView.as_view(), name='rest_login'),
    path('auth/logout/', LogoutView.as_view(), name='rest_logout'),
    path('auth/user/', UserDetailsView.as_view(), name='rest_user_details'),
    path('auth/password/change/', PasswordChangeView.as_view(), name='rest_password_change'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    path('auth/register/', RegisterView.as_view(), name='rest_register'),
]
