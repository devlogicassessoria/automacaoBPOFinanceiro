from fastapi import APIRouter, Request,HTTPException
from contaazul.services.contaAzulService import ContaAzulService

router = APIRouter()

service = ContaAzulService()

@router.get("/conta-azul/callback")
async def conta_azul_callback(request: Request):
    code = request.query_params.get("code")

    if not code:
        raise HTTPException(status_code=400, detail="Code não informado")

    service.handle_oauth_callback(code)
    return {
        "status": "Conta Azul autorizado com sucesso",
        "code": code
    }