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
