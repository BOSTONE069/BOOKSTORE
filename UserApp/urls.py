from django.urls import path
from .views import *



urlpatterns = [
    path('create', UserCreateApi),
    # path('login', UserLoginApi),
    path('protected', ProtectedUsersApi),
]