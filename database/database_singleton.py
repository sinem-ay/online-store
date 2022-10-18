from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from config import get_settings


class SingleInstanceMetaClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingleInstanceMetaClass, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Session(metaclass=SingleInstanceMetaClass):
    def __init__(self, db_url=None):
        if db_url:
            db_url = get_settings().db_url
        self.engine = create_engine(db_url, pool_pre_ping=True)
        self.session = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)

    def get_session(self):
        return self.session()

    def dispose(self):
        self.engine.dispose()


def get_db():
    db = Session().get_session()
    try:
        yield db
    finally:
        db.close()


Base = declarative_base()
