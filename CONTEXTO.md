# CONTEXTO DO PROJETO - Gestao de Assistencias

> INSTRUCAO PARA A IA: Este arquivo e a memoria do projeto.
> Sempre que o Leonardo iniciar uma nova conversa e colar este arquivo,
> leia tudo antes de responder e continue de onde paramos.

**Ultima atualizacao:** 27/09/2026 (madrugada)
**Responsavel:** Leonardo
**Status:** FASE 1 e FASE 2 concluidas - pronto para FASE 3 (rotas da API)

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
    ├── gestao.db           (banco SQLite - criado automaticamente)
    └── app/
        ├── __init__.py
        ├── config.py       (configuracoes)
        ├── database.py     (conexao SQLite)
        ├── models.py       (tabela OrdemServico)
        ├── main.py         (servidor FastAPI)
        ├── routers/
        │   └── __init__.py
        └── services/
            └── __init__.py

### Como rodar o servidor:

cd C:\gestao_assistencias\backend
venv\Scripts\activate
python -m app.main

Acessa: http://localhost:8000
Docs: http://localhost:8000/docs

---

## Proximas etapas da FASE 3 (Rotas da API)

1. Criar schemas.py (validacao Pydantic)
2. Criar routers/ordens.py com:
   - GET /api/ordens (listar todas)
   - GET /api/ordens/{id} (obter uma)
   - POST /api/ordens (criar)
   - PATCH /api/ordens/{id} (editar)
   - DELETE /api/ordens/{id} (deletar)
3. Registrar o router no main.py
4. Testar tudo no /docs

---

## O que ja foi aprendido

- O que e Git (controle de versao)
- O que e commit, git add, git push
- O que e .gitignore (e como adaptar da internet)
- O que e README.md, Markdown
- O que e requirements.txt (dependencias)
- O que e venv (ambiente virtual) e como ativar
- O que e pip install -r
- O que e config.py (configuracoes centralizadas)
- O que e database.py (conexao com SQLite)
- O que e SQLAlchemy (ORM)
- O que e Base, engine, SessionLocal
- O que e __init__.py (pacote Python)
- O que e models.py (tabelas em classes)
- O que e Column, Integer, String, Float, Boolean, DateTime, Text
- O que e primary_key, unique, index, default
- O que e FastAPI (app)
- O que e CORS
- O que e rota (@app.get)
- O que e uvicorn (servidor)
- Como rodar `python -m app.main`
- Como acessar http://localhost:8000

---

## O que falta aprender

- [ ] O que e schemas.py (Pydantic)
- [ ] O que e router (APIRouter)
- [ ] Como dividir rotas em arquivos
- [ ] O que e Depends (injecao de dependencia)
- [ ] O que e CRUD
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