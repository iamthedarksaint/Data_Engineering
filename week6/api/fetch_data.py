import requests
import pandas as pd
from datetime import datetime, timedelta
from prefect.client.schemas.schedules import IntervalSchedule
from decouple import config
from prefect import flow, task
from db import get_db
from models import TennisMatch
import random

@task
def sofascore() -> pd.DataFrame:
    url = "https://tennis-api-atp-wta-itf.p.rapidapi.com/tennis/v2/atp/h2h/matches/5992/677/"

    headers = {
	"x-rapidapi-key": config('apikey'),
	"x-rapidapi-host": "tennis-api-atp-wta-itf.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json().get('data')
    data = pd.json_normalize(data)
    df = pd.DataFrame(data)
    print(f"successfully loaded the dataframe")
    return df

@task
def clean(df: pd.DataFrame) -> pd.DataFrame:
    print(df.head(5))
    df = df
    return df
   

# @task    
def parquet(df: pd.DataFrame)-> None:
    try:
        print(df.head(2))
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') 
        df.to_parquet(f"week4/datalake/livescore_{timestamp}.parquet")
        print(f"Data saved as parquet file.")
    except Exception as e:
        print(f"Error saving to parquet: {e}")

@task
def csv(df: pd.DataFrame)-> None:
    try:
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') 
        df.to_csv(f"week4/datalake/livescore_{timestamp}.csv", index=False)
        print(f"Data saved as csv file.")
    except Exception as e:
        print(f"Error saving to csv: {e}" )

@task
def update(df: pd.DataFrame):
    tennis_db = get_db()

    db_data = [
        TennisMatch(
            id = random.randint(100, 10000),
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
            addition = row["player1Id"] + row["player2Id"]
        )
        for row in df.to_dict(orient='records')
    ]

    tennis_db.add_all(db_data)
    tennis_db.commit()
    print("Database updated successfully.") 

@flow
def main():
    data = sofascore()
    cleaned_data = clean(data)
    csv(cleaned_data)
    update(cleaned_data)
    

if __name__ == "__main__":
    main()
    # main.serve(schedules=[
    # IntervalSchedule(
    #   interval=timedelta(seconds=60),
    #     anchor_date=datetime(2024, 9, 29),
    #     timezone="America/Chicago"
    #     )
    # ]
    # )
    
    
