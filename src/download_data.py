# download_data.py
# Functions to fetch hourly electricity demand data from EIA API

import requests
import pandas as pd

def fetch_hourly_demand(api_key, start_date, end_date, region='PJM'):
    url = "https://api.eia.gov/v2/electricity/rto/region-data/data/"
    params = {
        "api_key": api_key,
        "frequency": "hourly",
        "data[0]": "value",
        "facets[respondent][]": region,
        "facets[type][]": "D",
        "start": start_date,
        "end": end_date
    }
    response = requests.get(url, params=params)
    data = response.json()
    df = pd.DataFrame(data["response"]["data"])
    df["period"] = pd.to_datetime(df["period"])
    df = df.sort_values("period").set_index("period")
    df = df.rename(columns={"value": "demand_MWh"})
    df["demand_MWh"] = pd.to_numeric(df["demand_MWh"], errors="coerce")
    df = df.dropna(subset=["demand_MWh"])
    return df
