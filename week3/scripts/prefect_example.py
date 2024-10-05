from prefect import flow, task
from datetime import timedelta, datetime
from prefect.client.schemas.schedules import IntervalSchedule


@flow
def my_flow(a, b) -> str:
    c = calculate(a, b)
    return f"Hello, world at {c}!"

@task(log_prints=False)
def calculate(a, b):
    print(a)
    return a + b

if __name__ == "__main__":
    my_flow.serve(parameters={'a':5, 'b':6}, schedules=[
    IntervalSchedule(
      interval=timedelta(seconds=10),
        anchor_date=datetime(2024, 9, 28),
        timezone="America/Chicago"
        )
    ]
    )
