from django.urls import path
from .views import *
urlpatterns = [
    path('signin/', user_login, name='signin'),
    path('register/', register, name='register'),
    path('logout/', custom_logout, name='logout'),
]

