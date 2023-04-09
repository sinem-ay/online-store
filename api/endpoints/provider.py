from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from schemas.provider import ProviderBase, ProviderCreate
from models import Provider, Base
from database.database_fast import SessionLocal, engine
from api import crud_provider

from database.database_fast import get_db

Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.get("/provider/{provider_id}", response_model=ProviderBase)
async def read_providers(
    provider_id: int, db: Session = Depends(get_db)
) -> List[Provider]:
    db_provider = crud_provider.get_provider(db, provider_id=provider_id)
    if db_provider is None:
        raise HTTPException(status_code=404, detail="Provider id not found")
    return db_provider


@router.get("/providers", response_model=List[ProviderBase])
async def read_providers(db: Session = Depends(get_db)) -> List[Provider]:
    return crud_provider.get_providers(db)
