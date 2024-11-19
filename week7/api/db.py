from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base

user = config("USER")
host = config("HOST")
port = config("PORT")
password = config("PASSWORD")
database = config("DATABASE")
db_url = f"postgresql://{user}:{password}@{host}:{port}/{database}"

# def get_db() -> scoped_session:
#   """
#   Connect to postgres
#   """
#   engine = create_engine(db_url, pool_size=1, max_overflow=1)
#   Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#   TennisSession = scoped_session(Session)

#   return TennisSession

engine = create_engine(db_url, pool_size=1, max_overflow=1)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
