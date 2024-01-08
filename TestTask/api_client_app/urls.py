"""
This script processes the request and calls the corresponding view.

Author: Roman
"""
from api_client_app.views import DomainCheck, DomainSave, EmailCheck, EmailSave, UserApiKeyActive, UsersApiKeyAPI
from django.urls import path

app_name: str = 'api'

urlpatterns = [
    path('v1/users_api_key', UsersApiKeyAPI.as_view(), name='users_api_key'),
    path('v1/users_api_key/<int:pk>', UsersApiKeyAPI.as_view(), name='users_api_key_change'),
    path('v1/users_api_key/<int:pk>/active', UserApiKeyActive.as_view(), name='users_api_key_change'),
    path('v1/email_check', EmailCheck.as_view(), name='email_check'),
    path('v1/email_save', EmailSave.as_view({'post': 'create'}), name='email_save'),
    path('v1/email_change/', EmailSave.as_view({'post': 'create'}), name='email_change'),
    path('v1/email_change/<int:pk>', EmailSave.as_view({'put': 'update', 'delete': 'destroy'})),
    path('v1/domain_check', DomainCheck.as_view(), name='domain_check'),
    path('v1/domain_save', DomainSave.as_view({'post': 'create'}), name='domain_save'),
    path('v1/domain_change/', DomainSave.as_view({'post': 'create'}), name='domain_change'),
    path('v1/domain_change/<int:pk>', DomainSave.as_view({'put': 'update', 'delete': 'destroy'})),

]