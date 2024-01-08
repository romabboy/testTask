"""
Django application configuration for the 'client_app' app.

This configuration provides settings for the 'client_app' app, including the default
auto field and the app name.

Author: Roman
"""

from django.apps import AppConfig


class ClientAppConfig(AppConfig):
    """Configuration class for the 'client_app' app."""

    default_auto_field = 'django.db.models.BigAutoField'
    name = 'client_app'
