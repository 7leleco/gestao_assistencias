# CONTEXTO DO PROJETO - Gestao de Assistencias

> INSTRUCAO PARA A IA: Este arquivo e a memoria do projeto.
> Sempre que o Leonardo iniciar uma nova conversa e colar este arquivo,
> leia tudo antes de responder e continue de onde paramos.

**Ultima atualizacao:** 27/09/2026 (noite)
**Responsavel:** Leonardo
**Status:** FASE 3 COMPLETA - CRUD de ordens funcionando!

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
- GitHub conectado

### FASE 2 CONCLUIDA! ✅
- [x] 2.1 a 2.12 - Estrutura base do backend completa
- config.py, database.py, models.py, main.py
- Tabela OrdemServico com 32 colunas
- Servidor FastAPI rodando

### FASE 3 CONCLUIDA! ✅
- [x] 3.1 - Criar schemas.py (OSBase, OSCreate, OSUpdate, OSOut) ✅
- [x] 3.2 - Criar routers/ordens.py com GET /api/ordens ✅
- [x] 3.3 - Registrar router no main.py ✅
- [x] 3.4 - Testar GET /api/ordens no /docs -> 200 OK! ✅
- [x] 3.5 - Adicionar GET /api/ordens/{id} -> 200 OK / 404 ✅
- [x] 3.6 - Adicionar POST /api/ordens -> 201 Created ✅
- [x] 3.7 - Adicionar PATCH /api/ordens/{id} -> 200 OK ✅
- [x] 3.8 - Adicionar DELETE /api/ordens/{id} -> 204 No Content ✅

### CRUD COMPLETO FUNCIONANDO! 🏆

| Rota | Metodo | Status |
|------|--------|--------|
| /api/ordens | GET | 200 OK |
| /api/ordens/{id} | GET | 200 OK / 404 |
| /api/ordens | POST | 201 Created |
| /api/ordens/{id} | PATCH | 200 OK |
| /api/ordens/{id} | DELETE | 204 No Content |

### Estrutura atual:

C:\gestao_assistencias\
├── .git/
├── .gitignore
├── README.md
├── requirements.txt
├── CONTEXTO.md
└── backend/
    ├── __init__.py
    ├── venv/
    ├── gestao.db
    ├── inserir_teste.py
    ├── ver_banco.py
    └── app/
        ├── __init__.py
        ├── config.py
        ├── database.py
        ├── models.py
        ├── schemas.py
        ├── main.py
        ├── routers/
        │   ├── __init__.py
        │   └── ordens.py
        └── services/
            └── __init__.py

### Como rodar o servidor:

cd C:\gestao_assistencias\backend
venv\Scripts\activate
python -m app.main

Acessa: http://localhost:8000
Docs: http://localhost:8000/docs

---

## PROXIMAS FASES

### FASE 4 - Frontend (site) - NAO COMECADO
- Pagina principal (index.html)
- Layout com sidebar
- Tabela de ordens
- Formulario de nova OS

### FASE 5 - Funcionalidades avancadas - NAO COMECADO
- Geracao de PDF
- Upload de fotos
- Parser Bradesco
- Checklist

### FASE 6 - Producao
- Deploy
- Login
- Backups automaticos

---

## O que ja foi aprendido

### Git e versionamento:
- O que e Git, commit, git add, git push
- O que e .gitignore, README.md, Markdown
- O que e branch main, commit hash
- O que e git remote add origin, git push --force

### Ambiente Python:
- O que e venv e como ativar
- O que e pip install -r
- O que e requirements.txt
- Como recriar o venv quando quebra

### Backend base:
- O que e config.py, database.py
- O que e SQLAlchemy (ORM)
- O que e Base, engine, SessionLocal
- O que e __init__.py
- O que e models.py
- O que e Column, Integer, String, Float, Boolean, DateTime, Text
- O que e primary_key, unique, index, default

### FastAPI:
- O que e FastAPI, CORS, rota (@app.get)
- O que e uvicorn (servidor)
- O que e schemas.py (Pydantic)
- O que e APIRouter
- O que e Depends
- O que e response_model
- O que e Optional
- O que e Path Parameter (/api/ordens/{id})
- O que e HTTPException (erro 404, 400)
- O que e status_code (200, 201, 204)
- O que e @router.get, @router.post, @router.patch, @router.delete
- Como testar rota no /docs

### Banco de dados:
- O que e SQL direto (INSERT INTO, SELECT)
- O que e .db (banco SQLite)
- Como ver o banco com script Python
- O que e db.add(), db.commit(), db.refresh()
- O que e db.delete()
- O que e exclude_unset=True
- O que e setattr

### Metaforas usadas:
- API = atendente da pizzaria
- Banco = cozinha (lanches)
- Models = ficha tecnica das pizzas
- Schemas = formulario de pedido
- Routers = telefones do atendente

---

## O que falta aprender

- [ ] O que e CRUD completo (COMPLETO!)
- [ ] O que e HTML/CSS/JS na pratica (FASE 4)
- [ ] O que e fetch (JS) (FASE 4)
- [ ] O que e PDF generation
- [ ] O que e upload de arquivos
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
- Schemas com campos Optional - Pra evitar erro 500
- 5 rotas do CRUD - GET todos, GET um, POST, PATCH, DELETE

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