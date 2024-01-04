"""
This script processes the request and calls the corresponding view.

Author: Roman
"""
from client_app.views import MainPage
from django.urls import path

app_name: str = 'main'

urlpatterns = [
    path('', MainPage.as_view(), name='home'),
]