"""
Configurações do projeto de Gestão de Assistências.
"""
from pathlib import Path

# ===== CAMINHOS DO PROJETO =====
# BASE_DIR = pasta raiz do backend (backend/)
BASE_DIR = Path(__file__).resolve().parent.parent

# Pasta onde as fotos serão salvas
UPLOADS_DIR = BASE_DIR / "uploads"

# ===== BANCO DE DADOS =====
# URL de conexão com SQLite (arquivo gestao.db na raiz do backend)
DATABASE_URL = f"sqlite:///{BASE_DIR / 'gestao.db'}"

# ==== CONFIGURAÇÕES DO APP =====
APP_NAME = "Gestão de Assistências"
APP_VERSION = "0.1.0"
DEBUG = True

# ===== TESTE TEMPORÁRIO =====
if __name__ == "__main__":
    print(f"BASE_DIR:      {BASE_DIR}")
    print(f"UPLOADS_DIR:   {UPLOADS_DIR}")
    print(f"DATABASE_URL:  {DATABASE_URL}")
    print(f"APP_NAME:      {APP_NAME}")
    print(f"APP_VERSION:   {APP_VERSION}")
    print(f"DEBUG:         {DEBUG}")