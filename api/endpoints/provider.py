from uuid import UUID
from typing import List
from fastapi import Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session

from schemas.provider import ProviderBase, ProviderCreate
from models import Provider, Base
from database.database_fast import SessionLocal, engine

from database.database_fast import get_db


Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.get('/provider/{provider_id}', response_model=ProviderBase)
async def read_product(
        provider_id: UUID, db: Session = Depends(get_db)
) -> List[Provider]:
    db_provider = db.query(Provider).filter(provider_id == provider_id).first()
    if db_provider is None:
        raise HTTPException(status_code=404, detail='Product not found')
    return db_provider


