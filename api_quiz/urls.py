from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('users/', show_users, name='show_users')
]