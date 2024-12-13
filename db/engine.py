from db.models import Base
from sqlalchemy.engine.base import Engine
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

engine: Engine = None
DBSession = sessionmaker()
 
def init_db(file: str):
    engine = create_engine(file)
    Base.metadata.bind = engine# Base is the instance that we import from models.py
    DBSession.configure(bind=engine)