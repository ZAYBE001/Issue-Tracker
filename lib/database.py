from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, User, Issue

DATABASE_URL = 'sqlite:///issue_tracker.db'

engine = create_engine(DATABASE_URL)
Session = sessionmaker(bind=engine)

def create_tables():
    Base.metadata.create_all(engine)