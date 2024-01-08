"""
This script provides connection between db and python.

Author: Roman
"""

from typing import TypeVar

from django.db import models

InstanceTypeUAK = TypeVar('InstanceTypeUAK', bound='MyUser')


class MyUser(models.Model):
    """Model representing a user with a session_id."""

    session_id: models.TextField = models.TextField(unique=True, null=True, blank=True)


class UsersApiKey(models.Model):
    """Model representing data related to API keys and users."""

    user: models.ForeignKey[MyUser] = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    api_key: models.TextField = models.TextField()
    active: models.BooleanField = models.BooleanField(default=False)

    def __str__(self: InstanceTypeUAK) -> str:
        """Convert instance to a string representation."""
        return f'{self.api_key}'


class UsersJson(models.Model):
    """Model representing data related to JSON responses and users."""

    user: models.ForeignKey[MyUser] = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    json_response: models.JSONField = models.JSONField()


class DomainJson(models.Model):
    """Model representing data related to domain and users."""

    user: models.ForeignKey[MyUser] = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    domain_json: models.JSONField = models.JSONField()
