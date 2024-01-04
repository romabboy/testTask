"""
This script provides connection between html forms and db.

Author: Roman
"""

from client_app.models import UsersApiKey
from django import forms
from django.db import models


class UsersApiKeyForm(forms.ModelForm):
    """This class create html form based on UserApiKey models."""

    class Meta:
        """This is Meta class to UserApiKeyForm."""

        model: models.Model = UsersApiKey
        fields = ['user', 'api_key']
        widgets = {
            'user':forms.TextInput(attrs={'class':'form-control','autocomplete':'off','hidden':True}),
            'api_key':forms.TextInput(attrs={'class':'form-control','autocomplete':'off'}),
        }
    