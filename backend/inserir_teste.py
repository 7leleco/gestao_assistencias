"""
Script TEMPORÁRIO pra inserir uma OS de teste.
NÃO é parte do projeto - só pra você ver funcionando.
"""
import sqlite3

# Conecta ao banco (a "cozinha")
conn = sqlite3.connect("gestao.db")
cursor = conn.cursor()

# Insere uma OS de teste (um "lanche" na gaveta)
cursor.execute("""
    INSERT INTO ordens (numero_os, seguradora, segurado, tipo_servico, prestador, cidade)
    VALUES (?, ?, ?, ?, ?, ?)
""", ("OS-TESTE-001", "Bradesco", "João Silva", "Elétrica", "Carlos", "Florianópolis"))

# Salva a mudança
conn.commit()
print("✅ OS de teste inserida no banco!")
print("Agora roda 'python ver_banco.py' de novo pra ver.")

# Fecha a conexão
conn.close()