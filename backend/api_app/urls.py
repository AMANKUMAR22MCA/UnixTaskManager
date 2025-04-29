from django.urls import path
from .views import RegisterView, LoginView, LogoutView, UserView
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path("me/", csrf_exempt(UserView.as_view()), name="me"),
]

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,    # For access token
    TokenRefreshView,       # For refresh token
)

urlpatterns += [
    # Obtain access token using username and password
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # Refresh the access token using the refresh token
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
