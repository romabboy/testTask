"""

This script is used to handle client side requests.

Author: Roman
"""

from typing import Any

from django.urls import reverse_lazy

from client_app.forms import UsersApiKeyForm
from django import forms
from django.http import HttpRequest, HttpResponse
from django.views.generic import FormView


class MainPage(FormView):
    """MainPage handles request from '/'."""

    template_name: str = 'client_app/main.html'
    form_class: forms.ModelForm = UsersApiKeyForm
    success_url = reverse_lazy('main:home')
    
    def form_valid(self: Any, form: Any) -> HttpResponse:
        request: HttpRequest = self.request
        
        if not request.session or not request.session.session_key:
            request.session.save()
        
        user_api: UsersApiKeyForm = form.save(commit=False)
        user_api.user = request.session.session_key

        user_api.save()
        
        return super().form_valid(form)

    