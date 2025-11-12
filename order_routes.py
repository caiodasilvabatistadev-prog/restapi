from urllib.request import Request

from fastapi import APIRouter

order_routes = APIRouter(prefix="/order", tags=["order"])
@order_routes.post("/servicos")
async def servicos():
    return {'VOCÊ ENTROU NA ROTA DE SERVIÇOS!'}

