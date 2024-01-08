"""

This script is used to handle api side requests.

Author: Roman
"""


from typing import List, Type, TypeVar, Union

from api_client_app.serializers import DomainJsonApi, UsersApiKeySerializer, UsersJsonApi
from api_client_app.services import HunterApi
from client_app.models import DomainJson, MyUser, UsersApiKey, UsersJson
from django.db.models.query import QuerySet
from rest_framework import generics, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

InstanceUsersApiKeyAPI = TypeVar('InstanceUsersApiKeyAPI', bound='UsersApiKeyAPI')
InstanceCheckUserApiKeyActive = TypeVar('InstanceCheckUserApiKeyActive', bound='UserApiKeyActive')
InstanceCheckEmailSave = TypeVar('InstanceCheckEmailSave', bound='EmailSave')
InstanceChangeEmailCheck = TypeVar('InstanceChangeEmailCheck', bound='EmailCheck')
InstanceChangeDomainCheck = TypeVar('InstanceChangeDomainCheck', bound='DomainCheck')
InstanceChangeDomainSave = TypeVar('InstanceChangeDomainSave', bound='DomainSave')


class UsersApiKeyAPI(generics.RetrieveUpdateDestroyAPIView):
    """UsersApiKeyAPI handles request from /api/v1/users_api_key."""

    serializer_class: Type[UsersApiKeySerializer] = UsersApiKeySerializer

    def get_queryset(self: InstanceUsersApiKeyAPI) -> Union[List[UsersApiKey], List[None]]:
        """Retrieve the queryset of UsersApiKey objects for the current user's session."""
        session_id: str = self.request.session.session_key
        user: MyUser = MyUser.objects.filter(session_id=session_id).first()

        return UsersApiKey.objects.filter(user=user)

    def put(self: InstanceUsersApiKeyAPI, request: Request, pk: int) -> Response:
        """Handle requests associated with the PUT method."""
        api_key: str = request.data.get('api_key')
        session_id: str = self.request.session.session_key
        user: MyUser = MyUser.objects.filter(session_id=session_id).first()

        if user:
            user_api: UsersApiKey = UsersApiKey.objects.filter(user=user, pk=pk).first()
            user_api.api_key = api_key
            user_api.save()

            response: Response = Response({'success': True})
        else:
            response: Response = Response({'success': False}, status=403)

        return response


class UserApiKeyActive(APIView):
    """UserApiKeyActive handles request from /api/v1/users_api_key/<int:pk>/active."""

    def put(self: InstanceCheckUserApiKeyActive, request: Request, pk: int) -> Response:
        """Handle requests associated with the PUT method."""
        session_id: str = request.session.session_key
        user: MyUser = MyUser.objects.filter(session_id=session_id).first()
        user_api_queryset: QuerySet[UsersApiKey] = UsersApiKey.objects.filter(user=user)

        response: dict = {}

        user_api_queryset.update(active=False)

        user_api: UsersApiKey = user_api_queryset.filter(pk=pk).first()

        if user_api:
            user_api.active = True
            user_api.save()
            response['success'] = True
        else:
            response['success'] = False

        return Response(response)


class EmailSave(viewsets.ModelViewSet):
    """EmailSave handles request from /api/v1/email_save, /api/v1/email_change."""

    serializer_class = UsersJsonApi

    def get_queryset(self: InstanceCheckEmailSave) -> Union[List[UsersJson], List[None]]:
        """Return queryset."""
        session_id: str = self.request.session.session_key
        user: MyUser = MyUser.objects.filter(session_id=session_id).first()

        return UsersJson.objects.filter(user=user)

    def create(self: InstanceCheckEmailSave, request: Request) -> Response:
        """Create a new UsersJson object."""
        json_response: str = request.data.get('json_response')
        session_id: str = self.request.session.session_key
        user: MyUser = MyUser.objects.filter(session_id=session_id).first()

        if user:
            UsersJson.objects.create(json_response=json_response, user=user)
            response: Response = Response({'success': True})
        else:
            response: Response = Response({'success': False}, status=403)

        return response


class EmailCheck(APIView):
    """EmailCheck handles request from /api/v1/email_check."""

    def get(self: InstanceCheckEmailSave, request: Request) -> Response:
        """Handle GET request to check email using Hunter API."""
        email: str = request.query_params.get('email')

        user: MyUser = MyUser.objects.filter(session_id=self.request.session.session_key).first()
        api: str = UsersApiKey.objects.filter(user=user, active=True).first().api_key
        hunter_response: dict = HunterApi.check_email(email, api)

        if hunter_response['data']:
            response: Response = Response(hunter_response)
        else:
            response: Response = Response({'api': True}, status=403)

        return response


class DomainCheck(APIView):
    """DomainCheck handles request from /api/v1/domain_check."""

    def get(self: InstanceCheckEmailSave, request: Request) -> Response:
        """Handle GET request to check domain using Hunter API."""
        domain: str = request.query_params.get('domain')

        session_id: str = self.request.session.session_key
        user: MyUser = MyUser.objects.filter(session_id=session_id).first()
        api: str = UsersApiKey.objects.filter(user=user, active=True).first().api_key
        hunter_response: dict = HunterApi.check_domain(domain, api)

        if hunter_response['data']:
            response: Response = Response(hunter_response)
        else:
            response: Response = Response({'api': True}, status=403)

        return response


class DomainSave(viewsets.ModelViewSet):
    """DomainSave handles request from /api/v1/domain_save, /api/v1/domain_change."""

    serializer_class = DomainJsonApi

    def get_queryset(self: InstanceChangeDomainSave) -> Union[QuerySet[DomainJson], List[None]]:
        """Return queryset."""
        session_id: str = self.request.session.session_key
        user: MyUser = MyUser.objects.filter(session_id=session_id).first()

        return DomainJson.objects.filter(user=user) if user else []

    def create(self: InstanceChangeDomainSave, request: Request) -> Response:
        """Create a new DomainJson object."""
        domain_json = request.data.get('domain_json')
        session_id = self.request.session.session_key
        user = MyUser.objects.filter(session_id=session_id).first()

        if user:
            DomainJson.objects.create(domain_json=domain_json, user=user)
            response = Response({'success': True})
        else:
            response = Response({'success': False}, status=403)

        return response


