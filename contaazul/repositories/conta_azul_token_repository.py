import json
from pathlib import Path
from datetime import datetime, timedelta

TOKEN_FILE = Path("storage/conta_azul_token.json")

class ContaAzulTokenRepository:
    def save(self, token: dict):
        TOKEN_FILE.parent.mkdir(exist_ok=True)
        token["saved_at"] = datetime.now().isoformat()
        TOKEN_FILE.write_text(json.dumps(token))

    def load(self) -> dict | None:
        if not TOKEN_FILE.exists():
            return None
        return json.loads(TOKEN_FILE.read_text())
    
    def is_expired(self, token: dict) -> bool:
        saved_at = datetime.fromisoformat(token["saved_at"])
        expires_at = token.get("expires_at", 0)
        return datetime.now() > saved_at + timedelta(seconds=expires_at - 60)
    
    
