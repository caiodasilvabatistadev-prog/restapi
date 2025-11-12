from fastapi import APIRouter

auth_routes = APIRouter(prefix="/auth", tags=["auth"])
@auth_routes.get("/lista")
async def pedidos():

    return{'mensagem: Você acessou a rota pedida'}
