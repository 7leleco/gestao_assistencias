"""
Schemas (validação) da API.
Cada classe aqui valida um tipo diferente de dados.
"""
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict


class OSBase(BaseModel):
    """Campos comuns a todos os schemas de OS."""
    numero_os: str
    seguradora: str
    segurado: str
    tipo_servico: str
    prestador: str
    status: str = "Aberta"
    telefone: str = ""
    email: str = ""
    cpf: str = ""
    endereco: str = ""
    bairro: str = ""
    cidade: str = ""
    uf: str = ""
    cep: str = ""
    motivo: str = ""
    origem: str = ""
    destino: str = ""
    distancia: str = ""
    observacoes: str = ""
    visita: float = 0.0
    mao_de_obra: float = 0.0
    pecas: float = 0.0
    valor_km: float = 0.0
    km_rodado: int = 0
    deslocamento: float = 0.0
    extras: float = 0.0
    pontos: int = 0
    valor_total: float = 0.0
    nota_feita: bool = False
    fotos: str = "[]"


class OSCreate(OSBase):
    """Schema para CRIAR uma OS (herda tudo de OSBase)."""
    pass


class OSUpdate(BaseModel):
    """Schema para ATUALIZAR uma OS (todos os campos opcionais)."""
    numero_os: Optional[str] = None
    seguradora: Optional[str] = None
    segurado: Optional[str] = None
    tipo_servico: Optional[str] = None
    prestador: Optional[str] = None
    status: Optional[str] = None
    telefone: Optional[str] = None
    email: Optional[str] = None
    cpf: Optional[str] = None
    endereco: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    uf: Optional[str] = None
    cep: Optional[str] = None
    motivo: Optional[str] = None
    origem: Optional[str] = None
    destino: Optional[str] = None
    distancia: Optional[str] = None
    observacoes: Optional[str] = None
    visita: Optional[float] = None
    mao_de_obra: Optional[float] = None
    pecas: Optional[float] = None
    valor_km: Optional[float] = None
    km_rodado: Optional[int] = None
    deslocamento: Optional[float] = None
    extras: Optional[float] = None
    pontos: Optional[int] = None
    valor_total: Optional[float] = None
    nota_feita: Optional[bool] = None
    fotos: Optional[str] = None


class OSOut(BaseModel):
    """Schema de RESPOSTA (todos os campos opcionais)."""
    id: int
    numero_os: Optional[str] = None
    seguradora: Optional[str] = None
    segurado: Optional[str] = None
    tipo_servico: Optional[str] = None
    prestador: Optional[str] = None
    status: Optional[str] = None
    telefone: Optional[str] = None
    email: Optional[str] = None
    cpf: Optional[str] = None
    endereco: Optional[str] = None
    bairro: Optional[str] = None
    cidade: Optional[str] = None
    uf: Optional[str] = None
    cep: Optional[str] = None
    motivo: Optional[str] = None
    origem: Optional[str] = None
    destino: Optional[str] = None
    distancia: Optional[str] = None
    observacoes: Optional[str] = None
    visita: Optional[float] = None
    mao_de_obra: Optional[float] = None
    pecas: Optional[float] = None
    valor_km: Optional[float] = None
    km_rodado: Optional[int] = None
    deslocamento: Optional[float] = None
    extras: Optional[float] = None
    pontos: Optional[int] = None
    valor_total: Optional[float] = None
    nota_feita: Optional[bool] = None
    fotos: Optional[str] = None
    data: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)