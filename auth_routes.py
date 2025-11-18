from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db_session import get_session
from models import User
from schemas import Userschema, LoginSchema
from security import bcrypt_context



auth_router = APIRouter(prefix="/auth", tags=["auth"])

# -- Rotas de criação de contas --

@auth_router.post("/criar_conta")
async def criar_conta(user_data: Userschema, session: Session = Depends(get_session)):
    # Verifica se já existe usuário com o mesmo email
    usuario_existente = session.query(User).filter(User.email == user_data.email).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail={"mensagem": "Já existe um usuário com esse email"})
    
    # Cria hash da senha
    hashed_password = bcrypt_context.hash(user_data.password)

    # Cria usuário
    novo_user = User(
        name=user_data.name,
        email=user_data.email,
        password=hashed_password,
        active=user_data.active if user_data.active is not None else True,
        admin=user_data.admin if user_data.admin is not None else False
    )

    session.add(novo_user)
    session.commit()
    session.refresh(novo_user)

    return {"mensagem": f"Usuário criado com sucesso: {user_data.email}"}


    # -- Rotas de login --
@auth_router.post("/login")
async def login(login_data: LoginSchema, session: Session = Depends(get_session)):
    usuario = session.query(User).filter(User.email == login_data.email).first()
async def login(credentials: LoginSchema, session: Session = Depends(get_session)):
    
    # Busca o usuário pelo email
    
    usuario = session.query(User).filter(User.email == credentials.email).first()
    
    # Verifica se o usuário existe e corresponde ao hash armazenado
    
    if not usuario or not bcrypt_context.verify(credentials.password, usuario.password):
        raise HTTPException(status_code=401, detail="Email ou senha inválidos")
    
    # RETORNO SUCESSO
    
    return {"mensagem": "Login realizado com sucesso",
        "usuario": {
            "id": usuario.id,
            "name": usuario.name,
            "email": usuario.email,
            "admin": usuario.admin
        }
    }