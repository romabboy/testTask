"""
This script processes the request and calls the corresponding view.

Author: Roman
"""
from client_app.views import ChangeData, ChangeDomain, ChangeEmail, CheckDomain, CheckEmail, MainPage
from django.urls import path

app_name: str = 'main'

urlpatterns = [
    path('', MainPage.as_view(), name='home'),
    path('check_email/', CheckEmail.as_view(), name='check_email'),
    path('check_domain/', CheckDomain.as_view(), name='check_domain'),
    path('change_data/', ChangeData.as_view(), name='change_data'),
    path('change_email/<int:pk>/', ChangeEmail.as_view(), name='change_email'),
    path('change_domain/<int:pk>/', ChangeDomain.as_view(), name='change_domain'),
]
