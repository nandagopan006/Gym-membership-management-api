from django.urls import path
from .views import SignupAPIView,LoginAPIView,ProfileAPIView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("signup/",SignupAPIView.as_view(),name="signup"),
    path("login/",LoginAPIView.as_view(),name="login"),
    path("profile/",ProfileAPIView.as_view(),name="profile"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token-refresh"),
    
]