import os
from dataclasses import dataclass

@dataclass(frozen=True)

class ContaAzulSettings:
    client_id: str
    client_secret: str
    redirect_uri: str

class Settings:
    def __init__(self):
        self.conta_azul = ContaAzulSettings(
            client_id=os.getenv("CONTA_AZUL_CLIENT_ID"),
            client_secret=os.getenv("CONTA_AZUL_CLIENT_SECRET"),
            redirect_uri=os.getenv("CONTA_AZUL_REDIRECT_URI"),
        )
        self._validate()

    def _validate(self):
        missing = []

        if not self.conta_azul.client_id:
            missing.append("CONTA_AZUL_CLIENT_ID")
        if not self.conta_azul.client_secret:
            missing.append("CONTA_AZUL_CLIENT_SECRET")
        if not self.conta_azul.redirect_uri:
            missing.append("CONTA_AZUL_REDIRECT_URI")
        
        if missing:
            raise RuntimeError(
                f"Variáveis não configuradas. {', '.join(missing)}"
            )
        
settings = Settings()
        
