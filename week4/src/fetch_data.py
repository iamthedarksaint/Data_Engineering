import requests
import pandas as pd
from datetime import datetime
from prefect.client.schemas.schedules import IntervalSchedule
from decouple import config
from prefect import flow, task
from datetime import timedelta, datetime

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
def excel(df: pd.DataFrame)-> None:
    try:
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S') 
        df.to_excel(f"week4/datalake/livescore_{timestamp}.xlsx", index=False, engine="openpyxl")
        print(f"Data saved as Excel file.")
    except Exception as e:
        print(f"Error saving to Excel: {e}" )

@flow
def main():
    data = sofascore()
    parquet(data)
    excel(data)

if __name__ == "__main__":
    main.serve(schedules=[
    IntervalSchedule(
      interval=timedelta(seconds=60),
        anchor_date=datetime(2024, 9, 29),
        timezone="America/Chicago"
        )
    ]
    )
    
    
