import requests
import pandas as pd
from datetime import datetime
from prefect.client.schemas.schedules import IntervalSchedule
from decouple import config
from prefect import flow, task
from datetime import timedelta, datetime
from db import get_db
from models import TennisMatch

@task
def sofascore() -> None:
    try:
        url = "https://tennis-api-atp-wta-itf.p.rapidapi.com/tennis/v2/atp/h2h/matches/5992/677/"

        headers = {
	    "x-rapidapi-key": config('apikey'),
	    "x-rapidapi-host": "tennis-api-atp-wta-itf.p.rapidapi.com"
    }
        response = requests.get(url, headers=headers)
        data = response.json()['data']
        data = pd.json_normalize(data)
        df = pd.DataFrame(data)
        return df 
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

@task    
def parquet(df: pd.DataFrame)-> None:
    try:
        print(df.head(2))
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') 
        df.to_parquet(f"week4/datalake/livescore_{timestamp}.parquet", engine="pyarrow")
        print(f"Data saved as parquet file.")
    except Exception as e:
        print(f"Error saving to parquet: {e}")

@task
def csv(df: pd.DataFrame)-> None:
    try:
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') 
        df.to_csv(f"week4/datalake/livescore_{timestamp}.csv", index=False, engine="openpyxl")
        print(f"Data saved as csv file.")
    except Exception as e:
        print(f"Error saving to csv: {e}" )

@task
def update(df: pd.DataFrame):
    tennis_db = get_db()

    db_data = [
        TennisMatch(
            id = row["id"],
            match_date = row["date"],
            roundId = row["roundId"],
            player1Id = row["player1Id"],
            player2Id = row["player2Id"],
            tournamentId = row["tournamentId"],
            match_winner = row["match_winner"],
            result = row["result"],
            player1_fullId = row["player1.id"],
            player1_name = row["player1.name"],
            player1_country_acr = row["player1.countryAcr"],
            player2_full_id = row["player2.id"],
            player2_name = row["player2.name"],
            player2_country_acr = row["player2.countryAcr"],
        )
        for row in df.to_dict(orient='records')
    ]

    tennis_db.add_all(db_data)
    tennis_db.commit()

@flow
def main():
    data = sofascore()
    parquet(data)
    csv(data)
    update(data)
    

if __name__ == "__main__":
    main.serve(schedules=[
    IntervalSchedule(
      interval=timedelta(seconds=5),
        anchor_date=datetime(2024, 9, 29),
        timezone="America/Chicago"
        )
    ]
    )
    
    
