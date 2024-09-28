import requests
import http.client
import json
import pandas as pd


r =  requests.get("https://rapidapi.com/Creativesdev/api/free-football-api-data/playground/apiendpoint_3f3466e5-be4d-451b-bdec-eac888dbd88c")
print(r.status_code)


conn = http.client.HTTPSConnection("free-football-api-data.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "73da526a6dmsh74387eb97413c99p17fc16jsn94ac1b7306ac",
    'x-rapidapi-host': "free-football-api-data.p.rapidapi.com"
}

conn.request("GET", "/football-current-number-of-live", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

json_data = json.loads(data.decode("utf-8"))
df = pd.json_normalize(json_data)
print(df)

df.to_csv('livescores.csv', index=False)
df.to_parquet('livescores.parquet', index=False)