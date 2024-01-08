"""

This script is used to handle client side requests.

Author: Roman
"""

from typing import Dict, Optional, TypeVar, Type

from client_app.forms import CheckDomainForm, CheckEmailForm, UsersApiKeyForm
from client_app.models import DomainJson, MyUser, UsersApiKey, UsersJson
from django import forms
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, FormView, TemplateView

InstanceMainPage = TypeVar('InstanceMainPage', bound='MainPage')
InstanceCheckEmail = TypeVar('InstanceCheckEmail', bound='CheckEmail')
InstanceCheckDomain = TypeVar('InstanceCheckDomain', bound='CheckDomain')
InstanceChangeData = TypeVar('InstanceChangeData', bound='ChangeData')


class MainPage(FormView):
    """MainPage handles request from '/'."""

    template_name: str = 'client_app/main.html'
    form_class: UsersApiKeyForm = UsersApiKeyForm
    success_url = reverse_lazy('main:home')

    def form_valid(self: InstanceMainPage, form: UsersApiKeyForm) -> HttpResponse:
        """Check form."""
        request: HttpRequest = self.request
     
        if not request.session or not request.session.session_key:
            request.session.save()

        user, is_created = MyUser.objects.get_or_create(session_id=request.session.session_key)

        UsersApiKey.objects.update(active=False)

        user_api: UsersApiKeyForm = form.save(commit=False)
        user_api.user = user
        user_api.active = True

        user_api.save()
  
        return super().form_valid(form)


class CheckEmail(TemplateView):
    """CheckEmail handles request from '/check_email'."""

    def get(self: InstanceCheckEmail, request: HttpRequest) -> HttpResponse:
        """Handels request that is asociated with get method."""
        context: Dict[str, forms.Form] = {}

        if not request.session or not request.session.session_key:
            context['form'] = UsersApiKeyForm()
            response: HttpResponse = render(request, 'client_app/api_required.html', context=context)
        elif UsersApiKey.objects.filter(user__session_id=request.session.session_key).exists():
            context['form'] = CheckEmailForm()
            response: HttpResponse = render(request, 'client_app/email_check.html', context=context)
        else:
            context['form'] = UsersApiKeyForm()
            response: HttpResponse = render(request, 'client_app/api_required.html', context=context)

        return response


class CheckDomain(TemplateView):
    """CheckEmail handles request from '/check_domain'."""

    def get(self: InstanceCheckDomain, request: HttpRequest) -> HttpResponse:
        """Handels request that is asociated with get method."""
        context: dict = {}

        if not request.session or not request.session.session_key:
            context['form'] = UsersApiKeyForm()
            response: HttpResponse = render(request, 'client_app/api_required.html', context=context)
        elif UsersApiKey.objects.filter(user__session_id=request.session.session_key):
            context['form'] = CheckDomainForm()
            response: HttpResponse = render(request, 'client_app/domain_check.html', context=context)
        else:
            context['form'] = UsersApiKeyForm()
            response: HttpResponse = render(request, 'client_app/api_required.html', context=context)

        return response


class ChangeData(TemplateView):
    """ChangeData handles request from '/change_data'."""

    def get(self: InstanceChangeData, request: HttpRequest) -> HttpResponse:
        """Handels request that is asociated with get method."""
        context: Dict[str, Optional[QuerySet]] = {'user_api': None, 'user_json': None, 'domains': None}

        user: Optional[MyUser] = MyUser.objects.filter(session_id=self.request.session.session_key).first()

        if user:
            context['user_api'] = UsersApiKey.objects.filter(user=user)
            context['user_json'] = UsersJson.objects.filter(user=user)
            context['domains'] = DomainJson.objects.filter(user=user)

            response: HttpResponse = render(request, 'client_app/change_data.html', context)
        else:
            response: HttpResponse = render(request, 'client_app/api_required.html')

        return response


class ChangeEmail(DetailView):
    """ChangeEmail handles request from '/change_email'."""

    template_name = 'client_app/change_email.html'
    context_object_name = 'email'
    model = UsersJson
    pk_url_kwarg = 'pk'


class ChangeDomain(DetailView):
    """ChangeDomain handles request from '/change_email'."""
 
    template_name = 'client_app/change_domain.html'
    context_object_name = 'domain'
    model = DomainJson
    pk_url_kwarg = 'pk'


def error_404_view(request: HttpRequest, exception: Type[BaseException]) -> HttpResponse:
    """Handle error 404."""
    return render(request, 'client_app/error_404.html', {'message': 'Page not found'})


def error_500_view(request: HttpRequest) -> HttpResponse:
    """Handle error 404."""
    return render(request, 'client_app/error_404.html', {'message': 'Server problem'})