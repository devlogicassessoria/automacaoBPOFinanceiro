from fastapi import FastAPI # pyright: ignore[reportMissingImports]

from contaazul.app.routes.endpoint_webhook import router as endpoint_router
from contaazul.app.routes.conta_azul_webhook import router as conta_azul_router

def create_app() -> FastAPI:
    app = FastAPI(title = "Integração ContaAzul")
    app.include_router(endpoint_router)
    app.include_router(conta_azul_router)
    print ("Deu certo!")

    return app

app = create_app()   