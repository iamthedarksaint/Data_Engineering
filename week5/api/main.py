from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Annotated
import models
from db import engine, SessionLocal
from pydantic import BaseModel
from datetime import date

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


class tennis_table(BaseModel):
  id: int
  match_date: date
  roundId: int 
  player1Id: int
  player2Id: int 
  tournamentId: int
  match_winner: int  
  result: str
  player1_fullId: int
  player1_name: str
  player1_country_acr: str 
  player2_full_id: int
  player2_name: str
  player2_country_acr: str 
  addition: int
  created_at: date
  updated_at: date

def get_db():
  my_db = SessionLocal()
  try:
    yield my_db
  finally:
    my_db.close()

db_dependencies = Annotated[Session, Depends(get_db)]

@app.get("/player")
async def all(db: db_dependencies):
  result = db.query(models.TennisMatch).all()
  return result

@app.get("/player/{player_id}")
async def get(player_id: int, db: db_dependencies):
  result = db.query(models.TennisMatch).filter(models.TennisMatch.id == player_id).first()
  if not result:
    raise HTTPException(status_code = 404, detail="Player not found")
  return result

@app.post("/player/")
async def add(player: tennis_table, db: db_dependencies):
  new_player = models.TennisMatch(
    id = player.id, 
    match_date = player.match_date,
    roundId = player.roundId,
    player1Id = player.player1Id,
    player2Id = player.player2Id,
    tournamentId = player.tournamentId,
    match_winner = player.match_winner,
    result = player.result,
    player1_fullId = player.player1_fullId,
    player1_name = player.player1_name,
    player1_country_acr = player.player1_country_acr,
    player2_full_id = player.player2_full_id,
    player2_name = player.player2_name,
    player2_country_acr = player.player2_country_acr,
    addition = player.addition,
    created_at = player.created_at,
    updated_at = player.updated_at
    )
  db.add(new_player)
  db.commit()
  db.refresh(new_player)
  return new_player


@app.put("/player/{player_id}")
async def update(player_id: int, player: tennis_table, db: db_dependencies):
  edit_player = db.query(models.TennisMatch).filter(models.TennisMatch.id ==  player_id).first()
  if not edit_player:
    raise HTTPException(status=404, detail="Player not found")
  edit_player.match_date = player.match_date
  edit_player.roundId = player.roundId
  edit_player.player1Id = player.player1Id
  edit_player.player2Id = player.player2Id
  edit_player.tournamentId = player.tournamentId
  edit_player.match_winner = player.match_winner
  edit_player.result = player.result
  edit_player.player1_fullId = player.player1_fullId
  edit_player.player1_name = player.player1_name
  edit_player.player1_country_acr = player.player1_country_acr
  edit_player.player2_full_id = player.player2_full_id
  edit_player.player2_name = player.player2_name
  edit_player.player2_country_acr = player.player2_country_acr
  edit_player.addition = player.addition
  edit_player.created_at = player.created_at
  edit_player.updated_at = player.updated_at
  
  db.commit()
  db.refresh(edit_player)
  
  return edit_player

@app.delete("/player/{player_id}")
async def delete(player_id: int, db: db_dependencies):
  existing_player = db.query(models.TennisMatch).filter(models.TennisMatch.id ==  player_id).first()
  if not existing_player:
    raise HTTPException(status=404, detail="Player not found")
  
  db.delete(existing_player)
  db.commit()
  return {"detail": "Player deleted successfully"}