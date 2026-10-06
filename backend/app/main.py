"""
Ponto de entrada do servidor FastAPI.
Este arquivo cria o app, registra as rotas e roda o servidor.
"""
from pathlib import Path

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.config import APP_NAME, APP_VERSION
from app.database import Base, engine
from app import models
from app.routers import ordens


# =====================================================
# CAMINHOS DO PROJETO
# =====================================================
FRONTEND_DIR = Path(__file__).resolve().parent.parent.parent / "frontend"


# =====================================================
# CRIA AS TABELAS NO BANCO
# =====================================================
Base.metadata.create_all(bind=engine)


# =====================================================
# CRIA O APP FASTAPI
# =====================================================
app = FastAPI(
    title=APP_NAME,
    version=APP_VERSION,
    description="Sistema de gestão de assistências técnicas",
)


# =====================================================
# CONFIGURA CORS
# =====================================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# =====================================================
# REGISTRA OS ROUTERS
# =====================================================
app.include_router(ordens.router)


# =====================================================
# SERVE ARQUIVOS ESTÁTICOS (CSS, JS, IMAGENS)
# =====================================================
app.mount(
    "/static",
    StaticFiles(directory=FRONTEND_DIR / "static"),
    name="static",
)


# =====================================================
# ROTAS DE TESTE
# =====================================================
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


# =====================================================
# ROTAS DE PÁGINAS (HTML)
# =====================================================
@app.get("/site", response_class=HTMLResponse)
def pagina_inicial():
    """Serve a página inicial do site (lista de assistências)."""
    caminho = FRONTEND_DIR / "index.html"
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()


@app.get("/nova-assistencia", response_class=HTMLResponse)
def pagina_nova_assistencia():
    """Serve a página de nova assistência (formulário)."""
    caminho = FRONTEND_DIR / "nova_assistencia.html"
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()


# =====================================================
# RODA O SERVIDOR
# =====================================================
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)