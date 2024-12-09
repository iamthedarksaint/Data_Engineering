from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

user = config("USER")
host = config("HOST")
password = config("PASSWORD")
database = config("DATABASE")
db_url = f"postgresql://{user}:{password}@{host}/{database}"

def get_db() -> scoped_session:
  """
  Connect to postgres
  """
  engine = create_engine(db_url, pool_size=1, max_overflow=1)
  Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
  TennisSession = scoped_session(Session)

  return TennisSession