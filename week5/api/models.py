from sqlalchemy import Column, BigInteger, DateTime, Integer,Text, func, String
from db import Base


class TennisMatch(Base):

  __tablename__ = "tennis_matches"

  id = Column(BigInteger, primary_key=True, nullable=False)
  match_date = Column(DateTime)
  roundId = Column(Integer)
  player1Id = Column(Integer)
  player2Id = Column(Integer)
  tournamentId = Column(Integer)
  match_winner = Column(Integer)
  result = Column(String)
  player1_fullId = Column(Integer)
  player1_name = Column(String)
  player1_country_acr = Column(String)
  player2_full_id = Column(Integer)
  player2_name = Column(String)
  player2_country_acr = Column(String)
  addition = Column(Integer)
  created_at = Column(DateTime, default=func.now())
  updated_at = Column(DateTime, default=func.now(), onupdate=func.now())


  







