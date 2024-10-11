import pandas as pd
import requests
import argparse
from decouple import config
from datetime import datetime
from prefect import flow, task
from datetime import timedelta, datetime
from prefect.client.schemas.schedules import IntervalSchedule

@task
def forever() -> pd.DataFrame:
    """
    Checks for tennis update
    """

    url = "https://tennis-api-atp-wta-itf.p.rapidapi.com/tennis/v2/atp/h2h/matches/5992/677/"

    headers = {
        "x-rapidapi-key": config('apikey'),
        "x-rapidapi-host": "tennis-api-atp-wta-itf.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    data = response.json()['data']

    df = pd.DataFrame(data)

    return df

@task
def clean(df: pd.DataFrame) -> pd.DataFrame:
    print(df.columns) 
    # TODO: algorithms to clean data based on specific needs
    df = df
    return df

@task
def store(df: pd.DataFrame) -> None:
    df.to_parquet(f'./tennis_{datetime.now()}.parquet', index=True)
    # TODO: configure proper naming conventions
    df.to_excel(f'./tennis_{datetime.now()}.xlsx')
    
@flow
def main():
    data = forever()
    cleaned_data = clean(data)
    store(cleaned_data)

if __name__=='__main__':
    main()
    # main.serve(schedules=[
    # IntervalSchedule(
    #   interval=timedelta(seconds=60),
    #     anchor_date=datetime(2024, 9, 28),
    #     timezone="America/Chicago"
    #     )
    # ]
    # )
