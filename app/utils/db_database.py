from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, NullPool
from app.config import DATABASE_URI


class MyDatabase:
    _engine = None
    _Session = None

    @classmethod
    def initialize(cls):
        if cls._engine is None:
            cls._engine = create_engine(DATABASE_URI, pool_pre_ping=True, pool_recycle=3600, poolclass=NullPool)
            cls._Session = sessionmaker(bind=cls._engine)

    @classmethod
    def get_session(cls):
        if cls._Session is None:
            cls.initialize()
        return cls._Session()
