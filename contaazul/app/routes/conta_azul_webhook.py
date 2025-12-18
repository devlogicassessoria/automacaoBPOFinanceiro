from fastapi import APIRouter, Request

router = APIRouter()

@router.get("/conta-azul/callback")
async def conta_azul_callback(request: Request):
    code = request.query_params.get("code")
    state = request.query_params.get("state")

    # DEBUG
    print("CODE:", code)
    print("STATE:", state)

    return {
        "status": "callback recebido",
        "code": code
    }