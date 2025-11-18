from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base

# Configuração do banco
DATABASE_URL = "sqlite:///database.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Cria factory de sessões
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Cria tabelas
Base.metadata.create_all(bind=engine)

# Função de dependência para FastAPI
def get_session() -> Session:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
