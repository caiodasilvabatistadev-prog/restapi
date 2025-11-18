from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base
from db_session import get_session
from passlib.context import CryptContext
for session in get_session():
    print(session)

# Cria o engine do banco
DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Cria factory de sessão
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria as tabelas no banco
Base.metadata.create_all(bind=engine)

# Função de dependência para FastAPI
def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
