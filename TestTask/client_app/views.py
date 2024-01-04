"""

This script is used to handle client side requests.

Author: Roman
"""
from django.views.generic import TemplateView


class MainPage(TemplateView):
    """MainPage handles request from '/'."""

    template_name = 'client_app/main.html'
