"""
This script provides connection between html forms and db.

Author: Roman
"""

from client_app.models import UsersApiKey
from django import forms


class UsersApiKeyForm(forms.ModelForm):
    """Form for UsersApiKey model."""

    class Meta:
        """Meta class for UsersApiKeyForm."""

        model: UsersApiKey = UsersApiKey
        fields: list = ['api_key']
        widgets: dict = {
            'api_key': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
        }


class CheckEmailForm(forms.Form):
    """Form for email checking."""

    email: forms.EmailField = forms.EmailField(
        label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
    )


class CheckDomainForm(forms.Form):
    """Form for domain checking."""

    domain: forms.CharField = forms.CharField(
        label='Domain', widget=forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
    )