from sqlalchemy import Column, BigInteger, DateTime, Integer,Text, String
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class TennisMatch(Base):

  __tablename__ = "tennis_matches"

  id = Column(BigInteger, primary_key=True, nullable=False)
  match_date = Column(DateTime)
  roundId = Column(Integer)
  player1Id = Column(Integer)
  player2Id = Column(Integer)
  tournamentId = Column(Integer)
  match_winner = Column(Integer)
  result = Column(Integer)
  player1_fullId = Column(Integer)
  player1_name = Column(Text)
  player1_country_acr = Column(Text)
  player2_full_id = Column(Integer)
  player2_name = Column(Text)
  player2_country_acr = Column(Text)


  







