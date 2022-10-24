from sqlalchemy.orm import Session

from uuid import UUID, uuid4
from models import Provider
from schemas.provider import ProviderBase, ProviderCreate


def get_providers(db: Session):
    return db.query(Provider).all()


def get_provider(db: Session, provider_id: int):
    return db.query(Provider).filter(provider_id == provider_id).first()


def create_provider_by_product():
    pass
