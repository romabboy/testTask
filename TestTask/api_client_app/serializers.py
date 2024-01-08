"""
Serializers for the client_app models.

This module provides serializers for Django models representing various data
related to API keys, JSON responses, and domain information.

author: Roman
"""

from client_app.models import DomainJson, UsersApiKey, UsersJson
from rest_framework import serializers


class UsersApiKeySerializer(serializers.ModelSerializer):
    """Serializer for the UsersApiKey model."""

    class Meta:
        """Meta class for UsersApiKeySerializer."""

        model = UsersApiKey
        fields = '__all__'


class UsersJsonApi(serializers.ModelSerializer):
    """Serializer for the UsersJson model."""

    json_response: serializers.JSONField = serializers.JSONField()

    class Meta:
        """Meta class for UsersJsonApi."""

        model = UsersJson
        fields = ['json_response']


class DomainJsonApi(serializers.ModelSerializer):
    """Serializer for the DomainJson model."""

    domain_json: serializers.JSONField = serializers.JSONField()

    class Meta:
        """Meta class for DomainJsonApi."""

        model = DomainJson
        fields = ['domain_json']