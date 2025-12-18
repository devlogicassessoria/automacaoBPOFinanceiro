from contaazul.clients.conta_azul_oauth_client import ContaAzulOAuthClient
from contaazul.repositories.conta_azul_token_repository import ContaAzulTokenRepository

class ContaAzulService:
    def __init__(self):
        self.oauth_client = ContaAzulOAuthClient()
        self.token_repository = ContaAzulTokenRepository()

    def handle_oauth_callback(self, code: str):
        token = self.oauth_client.exchange_code_for_token(code)
        self.token_repository.save(token)

    def get_valid_access_token(self) -> str:
        token = self.token_repository.load()

        if not token:
            raise Exception("Conta Azul não autorizado")
        
        if self.token_repository.is_expired(token):
            token = self.oauth_client.refresh_access_token(token["refresh_token"])
            self.token_repository.save(token)

        return token["access_token"]

