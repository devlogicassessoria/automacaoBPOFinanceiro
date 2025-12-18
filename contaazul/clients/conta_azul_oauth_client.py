import requests

from contaazul.core.config import settings


class ContaAzulOAuthClient:
    TOKEN_URL = "https://api.contaazul.com/oauth2/token"

    def exchange_code_for_token(self, code: str) -> dict:
        response = requests.post(
            self.TOKEN_URL,
            data={
                "grant_type": "authorization_code",
                "client_id": settings.conta_azul.client_id,
                "client_secret": settings.conta_azul.client_secret,
                "redirect_uri": settings.conta_azul.redirect_uri,
                "code": code,
            },
            timeout=10,
        )
        response.raise_for_status()
        return response.json()

    def refresh_access_token(self, refresh_token: str) -> str:
        response = requests.post(
            self.TOKEN_URL,
            data={
                "grant_type": "refresh_token",
                "client_id": settings.conta_azul.client_id,
                "client_secret": settings.conta_azul.client_secret,
                "refresh_token": refresh_token,
            },
            timeout=10,
        )
        response.raise_for_status()
        return response.json()
