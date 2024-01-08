"""
Django application configuration for the api_client_app.

author: Roman
"""

from django.apps import AppConfig


class ApiClientAppConfig(AppConfig):
    """Configuration class for the api_client_app."""
    
    default_auto_field: str = 'django.db.models.BigAutoField'
    name: str = 'api_client_app'
