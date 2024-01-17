from django.urls import path
from .views import *
urlpatterns = [
    path('total_amount/',total,name='total')
]