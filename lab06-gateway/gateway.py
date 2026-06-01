import time
import httpx

from fastapi import FastAPI, Request
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

app = FastAPI()
BASE_URL = "http://localhost:8000"

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


# MOCKS DE MICROSERVIÇOS INTERNOS (Simulando o Backend)
@app.get("/usuarios/me")
async def get_user():
    return {"id": 1, "nome": "Rafael Matsuyama", "perfil": "Premium"}


@app.get("/pedidos/recentes")
async def get_recent_orders():
    return {"itens": [{"id": 101, "total": 50.0}, {"id": 102, "total": 120.0}]}


# --- LAB 06: ENDPOINT VULNERÁVEL (BOT) ---
@app.get("/precos/lista")
@limiter.limit("5/second")
async def listar_precos(request: Request):
    # Atualmente sem Rate Limit! O aluno deverá proteger este endpoint.
    return {"precos": [10.0, 20.0, 30.0], "status": "desprotegido"}


# --- LAB 06: MISSÃO BFF (O aluno deve criar o /mobile-home) ---
@app.get("/mobile-home")
async def get_home_home():
    print("[GATEWAY] Consolidando dados para Mobile...")

    async with httpx.AsyncClient() as client:
        user_response = await client.get(f"{BASE_URL}/usuarios/me")
        orders_response = await client.get(f"{BASE_URL}/pedidos/recentes")

    return {
        "usuario": user_response.json(),
        "pedidos": orders_response.json()["itens"],
        "timestamp_gateway": time.time(),
    }
