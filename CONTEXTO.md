# CONTEXTO DO PROJETO - Gestao de Assistencias

> INSTRUCAO PARA A IA: Este arquivo e a memoria do projeto.
> Sempre que o Leonardo iniciar uma nova conversa e colar este arquivo,
> leia tudo antes de responder e continue de onde paramos.

**Ultima atualizacao:** 27/09/2026 (tarde)
**Responsavel:** Leonardo
**Status:** FASE 3 em andamento - 1 de 5 rotas da API feitas

---

## Sobre o projeto

- **Nome:** Gestao de Assistencias (JF Service)
- **Dono:** Leonardo
- **Objetivo:** Sistema interno para gerenciar assistencias tecnicas
- **Repositorio:** https://github.com/7leleco/gestao_assistencias
- **Meta pessoal:** Aprender a programar de verdade, nao so copiar codigo

---

## Stack (tecnologias)

- **Backend:** Python 3.14 + FastAPI + SQLite + SQLAlchemy
- **Frontend:** HTML + CSS + JavaScript puro (ainda nao comecado)
- **Editor:** VS Code
- **Controle de versao:** Git + GitHub

---

## Regras de aprendizado (IMPORTANTE!)

1. O Leonardo escreve o codigo - a IA orienta, revisa e corrige
2. Nada de codigo pronto - o Leonardo quer APRENDER, nao copiar
3. Explicar o PORQUE de cada coisa - nao so "faz isso"
4. Manter o CONTEXTO.md e APRENDIZADO.md atualizados - sempre
5. Nova conversa = colar o CONTEXTO.md - pra continuar de onde parou
6. Ir devagar e testar cada etapa - antes de avancar

---

## ESTADO ATUAL - 27/09/2026

### FASE 1 CONCLUIDA! ✅
- Git inicializado
- .gitignore completo
- README.md
- requirements.txt
- 3 commits feitos
- GitHub conectado

### FASE 2 CONCLUIDA! ✅
- [x] 2.1 - Criar pastas backend/app/routers/services ✅
- [x] 2.2 - Criar 4x __init__.py ✅
- [x] 2.3 - Criar config.py ✅
- [x] 2.4 - Testar config.py ✅
- [x] 2.5 - Criar database.py ✅
- [x] 2.6 - Instalar dependencias (venv + pip) ✅
- [x] 2.7 - Testar database.py ✅
- [x] 2.8 - Criar models.py (tabela OrdemServico com 32 colunas) ✅
- [x] 2.9 - Testar models.py ✅
- [x] 2.10 - Criar main.py ✅
- [x] 2.11 - Rodar servidor (uvicorn) ✅
- [x] 2.12 - Testar no navegador (JSON respondeu!) ✅

### FASE 3 EM ANDAMENTO! 🚧
- [x] 3.1 - Criar schemas.py (OSBase, OSCreate, OSUpdate, OSOut) ✅
- [x] 3.2 - Criar routers/ordens.py com GET /api/ordens ✅
- [x] 3.3 - Registrar router no main.py ✅
- [x] 3.4 - Testar GET /api/ordens no /docs -> 200 OK! ✅
- [ ] 3.5 - Adicionar GET /api/ordens/{id}
- [ ] 3.6 - Adicionar POST /api/ordens
- [ ] 3.7 - Adicionar PATCH /api/ordens/{id}
- [ ] 3.8 - Adicionar DELETE /api/ordens/{id}

### Estrutura atual:

C:\gestao_assistencias\
├── .git/
├── .gitignore
├── README.md
├── requirements.txt
├── CONTEXTO.md
└── backend/
    ├── __init__.py
    ├── venv/               (ambiente virtual)
    ├── gestao.db           (banco SQLite)
    ├── inserir_teste.py    (script de teste)
    ├── ver_banco.py        (script de teste)
    └── app/
        ├── __init__.py
        ├── config.py       (configuracoes)
        ├── database.py     (conexao SQLite)
        ├── models.py       (tabela OrdemServico)
        ├── schemas.py      (validacao Pydantic)
        ├── main.py         (servidor FastAPI)
        ├── routers/
        │   ├── __init__.py
        │   └── ordens.py   (rotas de OS)
        └── services/
            └── __init__.py

### Como rodar o servidor:

cd C:\gestao_assistencias\backend
venv\Scripts\activate
python -m app.main

Acessa: http://localhost:8000
Docs: http://localhost:8000/docs

---

## FASE 3 - Rotas da API (EM ANDAMENTO)

### Rotas que ja existem:

- GET /              (raiz - mostra info do app)
- GET /health        (health check)
- GET /api/ordens    (listar todas as OS)

### Rotas que faltam:

- GET /api/ordens/{id}      (obter uma OS)
- POST /api/ordens          (criar OS)
- PATCH /api/ordens/{id}    (editar OS)
- DELETE /api/ordens/{id}   (deletar OS)

### Testado e funcionando:

- GET /api/ordens -> retorna a OS "OS-TESTE-001" com 32 campos
- /docs mostra a rota automaticamente
- Schemas OSOut com campos opcionais

### Proximo passo:

- Adicionar as 4 rotas restantes (GET por id, POST, PATCH, DELETE)

---

## O que ja foi aprendido

### Git e versionamento:
- O que e Git (controle de versao)
- O que e commit, git add, git push
- O que e .gitignore (e como adaptar da internet)
- O que e README.md, Markdown
- O que e branch main
- O que e commit hash
- O que e git remote add origin
- O que e git push --force

### Ambiente Python:
- O que e venv (ambiente virtual) e como ativar
- O que e pip install -r
- O que e requirements.txt (dependencias)
- Como recriar o venv quando quebra

### Backend base:
- O que e config.py (configuracoes centralizadas)
- O que e database.py (conexao com SQLite)
- O que e SQLAlchemy (ORM)
- O que e Base, engine, SessionLocal
- O que e __init__.py (pacote Python)
- O que e models.py (tabelas em classes)
- O que e Column, Integer, String, Float, Boolean, DateTime, Text
- O que e primary_key, unique, index, default

### FastAPI:
- O que e FastAPI (app)
- O que e CORS
- O que e rota (@app.get)
- O que e uvicorn (servidor)
- Como rodar `python -m app.main`
- Como acessar http://localhost:8000
- O que e schemas.py (Pydantic) - validacao de dados
- O que e APIRouter (agrupa rotas por assunto)
- O que e Depends (injecao de dependencia)
- O que e response_model (formato da resposta)
- O que e Optional (campos que aceitam None)
- Como testar rota no /docs
- Como o FastAPI gera docs automaticas
- Erro comum: 2 classes com mesmo nome (uma sobrescreve a outra)

### Banco de dados:
- O que e SQL direto (INSERT INTO, SELECT)
- O que e .db (banco SQLite)
- Como ver o banco com script Python

### Metaforas usadas:
- API = atendente da pizzaria
- Banco de dados = cozinha (onde ficam os lanches)
- Models = ficha tecnica das pizzas
- Schemas = formulario de pedido
- Routers = telefones do atendente

---

## O que falta aprender

- [ ] O que e CRUD completo (ja fizemos "R")
- [ ] Como criar OS via API (POST)
- [ ] Como editar OS via API (PATCH)
- [ ] Como deletar OS via API (DELETE)
- [ ] O que e git branch e merge
- [ ] O que e HTML/CSS/JS na pratica
- [ ] O que e fetch (JS)
- [ ] O que e deploy
- [ ] O que e testes automatizados

---

## Comandos importantes

### Ativar venv (TODA VEZ que abrir terminal)

cd C:\gestao_assistencias\backend
venv\Scripts\activate

### Rodar servidor

python -m app.main

### Parar servidor

Ctrl + C

### Reiniciar servidor (depois de mudar codigo)

1. Ctrl + C (para)
2. python -m app.main (roda de novo)

### Ver banco

python ver_banco.py

### Inserir OS de teste

python inserir_teste.py

### Git - fluxo do dia a dia

cd C:\gestao_assistencias
git status
git add .
git commit -m "msg"
git push

---

## Decisoes tomadas

- Recomecar do zero - Pra aprender de verdade
- Leonardo escreve o codigo - Pra fixar o aprendizado
- Backend em app/ com routers - Padrao profissional
- Frontend separado em static/ - Boa pratica
- Paleta azul (marinho + royal) - Identidade visual
- Sidebar a esquerda - Layout profissional
- Backup antes de tudo - Seguranca
- Git desde o inicio - Padrao de mercado
- Rodar servidor como modulo (python -m app.main) - Padrao Python
- Schemas com campos Optional - Pra evitar erro 500 quando dados sao None

---

## Backup e seguranca

- Backup local: C:\backup_gestao_2026-09-26\
- GitHub: https://github.com/7leleco/gestao_assistencias
- Banco antigo: C:\backup_gestao_2026-09-26\backend\gestao.db.backup

---

## Como pedir ajuda a IA

Se voce travou em algum passo, use este template:

Leonardo, travei aqui:
- Fase: [qual fase]
- Passo: [qual passo]
- Erro que aparece: [cola o erro exato]
- O que eu tentei: [o que voce fez]

---

## LEMBRETE PARA NOVA CONVERSA

Quando esta conversa acabar:

1. Abra este arquivo (CONTEXTO.md)
2. Ctrl + A -> Ctrl + C (copia tudo)
3. Cole na primeira mensagem da nova conversa
4. Diga: "Leonardo, continua de onde paramos"

Sem isso, a IA nao sabe onde voce parou. Sempre cole o arquivo.

---

Fim do CONTEXTO.md - Mantenha este arquivo atualizado!