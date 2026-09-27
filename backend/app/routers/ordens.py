"""
Rotas de API para Ordens de Serviço (OS).
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app import models, schemas


router = APIRouter(
    prefix="/api/ordens",
    tags=["Ordens de Serviço"],
)


@router.get("", response_model=List[schemas.OSOut])
def listar_ordens(db: Session = Depends(get_db)):
    """Lista todas as ordens de serviço."""
    ordens = db.query(models.OrdemServico).all()
    return ordens


@router.get("/{os_id}", response_model=schemas.OSOut)
def obter_ordem(os_id: int, db: Session = Depends(get_db)):
    """Busca UMA ordem específica pelo ID."""
    os = db.query(models.OrdemServico).filter_by(id=os_id).first()
    if not os:
        raise HTTPException(status_code=404, detail="OS não encontrada")
    return os


@router.post("", response_model=schemas.OSOut, status_code=201)
def criar_ordem(dados: schemas.OSCreate, db: Session = Depends(get_db)):
    """Cria uma nova ordem de serviço."""
    #Verificar se já existe OS com esse número
    existe = db.query(models.OrdemServico).filter_by(numero_os=dados.numero_os).first()
    if existe:
        raise HTTPException(status_code=400, detail="já existe uma OS com esse número")

    # Cria a nova OS 
    nova_os = models.OrdemServico(**dados.model_dump())
    db.add(nova_os)
    db.commit()
    db.refresh(nova_os)
    return nova_os



@router.patch("/{os_id}", response_model=schemas.OSOut)
def editar_ordem(os_id: int, dados: schemas.OSUpdate, db: Session = Depends(get_db)):
    """Edita uma OS existente (só os campos enviados)."""
    os = db.query(models.OrdemServico).filter_by(id=os_id).first()
    if not os:
        raise HTTPException(status_code=404, detail="OS não encontrada")

    # Atualiza só os campos que foram enviados
    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(os, campo, valor)

    db.commit()
    db.refresh(os)
    return os


@router.delete("/{os_id}", status_code=204)
def deletar_ordem(os_id: int, db: Session = Depends(get_db)):
    """Deleta uma OS existente."""
    os = db.query(models.OrdemServico).filter_by(id=os_id).first()
    if not os:
        raise HTTPException(status_code=404, detail="OS não encontrada")

    db.delete(os)
    db.commit()
    return None