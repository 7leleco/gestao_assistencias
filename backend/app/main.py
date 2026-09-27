"""
Ponto de entrada do servidor FastAPI.
Este arquivo cria o app e roda o servidor.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import APP_NAME, APP_VERSION
from app.database import Base, engine
from app import models

# ===== CRIA AS TABELAS NO BANCO =====
Base.metadata.create_all(bind=engine)

# ===== CRIA O APP FASTAPI =====
app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Sistema de gestão de assistências técnicas",
)

# ===== CONFIGURA CORS =====
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ===== ROTAS DE TESTE =====
@app.get("/")
def raiz():
    """Rota raiz - mostra informações do app."""
    return {
        "app": APP_NAME,
        "versao": APP_VERSION,
        "status": "online",
    }


@app.get("/health")
def health():
    """Rota de saúde - pra saber se o servidor tá de pé."""
    return {"status": "ok"}


# ===== RODA O SERVIDOR =====
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)