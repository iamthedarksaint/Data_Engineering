import requests
import json
import pandas as pd

def sofascore(url, headers) -> None:
    try:
        response = requests.get(url, headers=headers)
        data = response.json()
        print(json.dumps(data, indent=4))
        return data
        # json_data = json.loads(data.decode("utf-8"))
        # data = pd.json_normalize(json_data)
        # return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def parquet(data, parquet_file_path):
    try:
        df = pd.DataFrame(data)
        df.to_parquet(parquet_file_path, engine="pyarrow")
        print(f"Data saved as parquet file: {parquet_file_path}")
    except Exception as e:
        print(f"Error saving to parquet: {e}")

def excel(data, xlsx_file_path):
    try:
        df = pd.DataFrame(data)
        df.to_excel(xlsx_file_path, index=False, engine="openpyxl")
        print(f"Data saved as Excel file: {xlsx_file_path}")
    except Exception as e:
        print(f"Error saving to Excel: {e}" )

if __name__ == "__main__":
    url = "https://tennis-api-atp-wta-itf.p.rapidapi.com/tennis/v2/atp/h2h/matches/5992/677/"

    headers = {
	"x-rapidapi-key": "73da526a6dmsh74387eb97413c99p17fc16jsn94ac1b7306ac",
	"x-rapidapi-host": "tennis-api-atp-wta-itf.p.rapidapi.com"
    }

    data = sofascore(url, headers)
    print(f"This is data: {data}")
    if data:
        parquet(data, 'week3/data/livescore.parquet')
        excel(data, "week3/data/livescore.xlsx")
    
