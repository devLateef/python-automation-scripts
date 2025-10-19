import requests
import pandas as pd
from datetime import datetime
import time

LAT = 7.3775   # Ibadan Latitude
LON = 3.9470   # Ibadan Longitude
YEAR = 2024
OUT_FILE = "./weather_datasets/oyo_weather_2024.csv"

BASE_URL = "https://power.larc.nasa.gov/api/temporal/hourly/point"

#NASA weather parameters
PARAMETERS = ",".join([
    "T2M",      
    "T2MDEW","T2MWET",               
    "RH2M",                          
    "WS10M","WD10M","WS50M","WD50M",
    "ALLSKY_SFC_SW_DWN","ALLSKY_SFC_LW_DWN",
    "ALLSKY_KT","PRECTOTCORR",      
    "PS","CLOUD_AMT","TOA_SW_DWN"
])

def fetch_month(year, month):
    start_date = f"{year}{month:02d}01"
    end_date = f"{year}{month:02d}28"

    params = {
        "latitude": LAT,
        "longitude": LON,
        "start": start_date,
        "end": end_date,
        "parameters": PARAMETERS,
        "community": "RE",
        "format": "JSON"
    }

    print(f"📡 Fetching {datetime(year, month, 1).strftime('%B %Y')}...")
    r = requests.get(BASE_URL, params=params)
    if r.status_code != 200:
        print(f"Failed for {month:02d}/{year} — Status {r.status_code}")
        print(r.text[:200])
        return None

    data = r.json()
    if "properties" not in data or "parameter" not in data["properties"]:
        print(f"Unexpected data format for {month:02d}/{year}")
        return None

    param_dict = data["properties"]["parameter"]
    df = pd.DataFrame(param_dict)
    df.index.name = "timestamp"
    df.reset_index(inplace=True)
    df["datetime"] = pd.to_datetime(df["timestamp"].astype(str), format="%Y%m%d%H")

    cols = ["datetime"] + [c for c in df.columns if c not in ["timestamp", "datetime"]]
    df = df[cols]

    for c in df.columns:
        if c != "datetime":
            df[c] = pd.to_numeric(df[c], errors="coerce")

    print(f"Retrieved {len(df)} records for {datetime(year, month, 1).strftime('%B %Y')}")
    return df


# Pipeline
all_months = []
for m in range(1, 13):
    try:
        df_month = fetch_month(YEAR, m)
        if df_month is not None:
            all_months.append(df_month)
        time.sleep(2)
    except Exception as e:
        print(f"Error fetching month {m}: {e}")
        continue

if all_months:
    df_all = pd.concat(all_months).sort_values("datetime").reset_index(drop=True)
    df_all.to_csv(OUT_FILE, index=False)
    print(f"\nSuccessfully saved full year data ({len(df_all)} records) to '{OUT_FILE}'")
else:
    print("No data fetched for any month.")
