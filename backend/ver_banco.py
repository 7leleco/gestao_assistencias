"""
Script TEMPORÁRIO só pra ver o que tem no banco.
NÃO é parte do projeto - é só pra visualizar.
"""
import sqlite3

# Conecta ao banco
conn = sqlite3.connect("gestao.db")
cursor = conn.cursor()

# Lista as tabelas
print("=" * 50)
print("TABELAS NO BANCO:")
print("=" * 50)
cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
tabelas = cursor.fetchall()
for t in tabelas:
    print(f"  - {t[0]}")

# Mostra a estrutura da tabela 'ordens'
print()
print("=" * 50)
print("COLUNAS DA TABELA 'ordens':")
print("=" * 50)
cursor.execute("PRAGMA table_info(ordens)")
colunas = cursor.fetchall()
for c in colunas:
    print(f"  - {c[1]} ({c[2]})")

# Mostra os dados
print()
print("=" * 50)
print("DADOS NA TABELA 'ordens':")
print("=" * 50)
cursor.execute("SELECT * FROM ordens LIMIT 5")
dados = cursor.fetchall()
if dados:
    for d in dados:
        print(f"  {d}")
else:
    print("  (nenhum dado ainda)")

conn.close()