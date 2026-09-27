"""
Configuração do banco de dados SQLite com SQLAlchemy.
Este arquivo cria a conexão com o banco e fornece sessões.
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from app.config import DATABASE_URL

# ===== ENGINE (motor do banco) =====
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=False
)

# ===== SESSÃO =====
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# ===== BASE (para os models) =====
Base = declarative_base()


# ===== DEPENDÊNCIA (para usar nas rotas) =====
def get_db():
    """Fornece uma sessão do banco pra cada requisição."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()