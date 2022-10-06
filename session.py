from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from typing import Generator

from config import Settings

engine = create_engine(Settings().database_url, pool_pre_ping=True)


def create_session() -> scoped_session:
    session = scoped_session(
        sessionmaker(autocommit=False, autoflush=False, bind=engine)
    )
    return session


def get_session() -> Generator[scoped_session, None, None]:
    session = create_session()
    try:
        yield session
    finally:
        session.close()
