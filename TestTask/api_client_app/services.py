"""
This code provide service for interaction between server and hunter.io.

author: Roman
"""

from __future__ import annotations

import requests


class HunterApi:
    """HunterApi provide service for interaction between server and hunter.io."""

    @classmethod
    def check_email(cls: HunterApi, email: str, api: str) -> dict:
        """Check email using Hunter API."""
        url: str = f'https://api.hunter.io/v2/email-verifier?email={email}&api_key={api}'
        response: requests.Request = requests.get(url, timeout=10)

        if response.ok:
            response: dict = response.json()
        else:
            response: dict = {'data': None}

        return response

    @classmethod
    def check_domain(cls: HunterApi, domain: str, api: str) -> dict:
        """Check domain using Hunter API."""
        url: str = f'https://api.hunter.io/v2/domain-search?domain={domain}&api_key={api}'
        response: requests.Request = requests.get(url, timeout=10)

        if response.ok:
            response: dict = response.json()
        else:
            response: dict = {'data': None}

        return response