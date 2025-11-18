from fastapi import APIRouter

order_router = APIRouter(prefix="/orders",tags=["orders"]
)

@order_router.get("/")
async def pedidos():
    return {"mensagem": "Você está na rota de autenticação","autenticado": False}