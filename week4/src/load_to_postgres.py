import pandas as pd
from sqlalchemy import create_engine

db_url = "postgresql://postgres:postgres@localhost:5432/my_db"
engine = create_engine(db_url)

excel = "week4/datalake/livescore_2024-10-05_13-58-21.xlsx"

try:
    df = pd.read_excel(excel)
except Exception as e:
    print(f"Error reading file {e}")

table_name = "livescores"

try:
    df.to_sql(table_name, engine, if_exists="replace", index=False)
    print(f"Data from {excel} has been loaded into table {table_name}.")
except Exception as e:
    print(f"Error writing {table_name} to database: {str(e)}")

print("The excel file has been processed and loaded into the PostgreSQL database.")