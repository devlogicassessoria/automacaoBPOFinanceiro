import json
import logging
from fastapi import APIRouter, Request

router = APIRouter(prefix="/webhooks/conta-azul")

logging.basicConfig(level=logging.INFO)

@router.post("")

async def receiveEvent(request: Request):
    payload = await request.json()

    logging.info("Webhook Conta Azul recebido:")
    logging.info(json.dumps(payload, indent = 2, ensure_ascii = False))

    return {"status": "ok"}
