from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

user = config("USER")
host = config("HOST")
password = config("PASSWORD")
database = config("DATABASE")
db_url = f"postgresql://{user}:{password}@{host}/{database}"

engine = create_engine(db_url, pool_size=1, max_overflow=1)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
