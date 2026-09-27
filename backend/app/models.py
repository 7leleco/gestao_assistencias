"""
Modelos (tabelas) do banco de dados.
"""
from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Text
from app.database import Base

class OrdemServico(Base):
    """Tabela de ordens de serviço (assistências)"""
    __tablename__= "ordens"

    # ===== IDENTIFICAÇÃO =====
    id = Column(Integer, primary_key=True, index=True)
    numero_os = Column(String(50), unique=True, index=True)

    # ===== DADOS DA OS =====
    seguradora = Column(String(100))
    segurado = Column(String(150))
    tipo_servico = Column(String(100))
    prestador = Column(String(150))
    status = Column(String(50), default="Aberta")

    # ===== CONTATO =====
    telefone = Column(String(30))
    email = Column(String(100))
    cpf = Column(String(20))

    # ===== ENDEREÇO =====
    endereco = Column(String(200))
    bairro = Column(String(100))
    cidade = Column(String(100))
    uf = Column(String(2))
    cep = Column(String(10))

    # ===== DETALHES =====
    motivo = Column(String(200))
    origem = Column(String(200))
    destino = Column(String(200))
    distancia = Column(String(20))
    observacoes = Column(Text)

    # ===== VALORES =====
    visita = Column(Float, default=0.0)
    mao_de_obra = Column(Float, default=0.0)
    pecas = Column(Float, default=0.0)
    valor_km = Column(Float, default=0.0)
    km_rodado = Column(Integer, default=0)
    deslocamento = Column(Float, default=0.0)
    extras = Column(Float, default=0.0)
    pontos = Column(Integer, default=0)
    valor_total = Column(Float, default=0.0)

    # ===== NOTAS FISCAL =====
    nota_feita = Column(Boolean, default=False)

    # ===== FOTOS =====
    fotos = Column(Text, default="[]")

    # ===== TIMESTAMP =====
    data = Column(DateTime, default=datetime.now)