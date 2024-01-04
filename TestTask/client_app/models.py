"""
This script provides connection between db and python.

Author: Roman
"""

from django.db import models


class UsersApiKey(models.Model):
    """This class create, handle data that is related with api key and users."""
    
    user: models.TextField = models.TextField(null=True, blank=True)
    api_key: models.TextField = models.TextField()
    
    def __str__(self) -> str:
        return f'{self.user} -> {self.api_key}'