from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List, Annotated
import models
from db import engine, SessionLocal
from pydantic import BaseModel
from datetime import date, datetime
from sqlalchemy import inspect
import uvicorn

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


@app.put("/player/{player_id}/update-column")
async def update(player_id: int, column_name: str, new_value: str, db: db_dependencies):
  edit_player = db.query(models.TennisMatch).filter(models.TennisMatch.id ==  player_id).first()

  if not edit_player:
    raise HTTPException(status=404, detail="Player not found")

  mapper = inspect(models.TennisMatch)
  column = mapper.columns.get(column_name)

  if column is None:
    raise HTTPException(status_code=400, detail=f"Column '{column_name}' not in the database.")

  if isinstance(column.type.python_type, type):
    column_type = column.type.python_type

    try:
      if column_type == int:
        new_value = int(new_value)
      elif column_type == str:
        new_value = str(new_value)
      elif column_type == date:
        new_value = datetime.fromisoformat(new_value).date()
      else:
        raise HTTPException(status_code=400, detail=f"Unsupported data type: {column_type}")
    except ValueError as e:
      raise HTTPException(status_code=400, detail=f"Invalid column value for {column_type.__name__}: {e}")
  
  setattr(edit_player, column_name, new_value)
  
  db.commit()
  db.refresh(edit_player)
  
  return edit_player

@app.delete("/player/{player_id}")
async def delete(player_id: int, db: db_dependencies):
  existing_player = db.query(models.TennisMatch).filter(models.TennisMatch.id ==  player_id).first()
  if not existing_player:
    raise HTTPException(status=404, detail="Player not f2ound")
  
  db.delete(existing_player)
  db.commit()
  return {f"detail": "Player with {player_id} deleted successfully"}

if __name__ == "__main__":
  uvicorn.run("main:app",
  host = "0.0.0.0", port=8000, reload=True)