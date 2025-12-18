from fastapi import FastAPI

from app.routes.endpoint_webhook import router as endpoint_router
from app.routes.conta_azul_webhook import router as conta_azul_router

app = FastAPI()

app.include_router(endpoint_router)
app.include_router(conta_azul_router)
