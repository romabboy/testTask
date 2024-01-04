"""
This script processes the request and calls the corresponding view.

Author: Roman
"""
from client_app.views import MainPage
from django.urls import path

app_name: str = 'api'

urlpatterns = [
    path('v1/', MainPage.as_view(), name='home'),
]