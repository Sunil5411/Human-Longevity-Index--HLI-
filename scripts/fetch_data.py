import requests
import pandas as pd
import os

indicators = {
    'life_expectancy': 'SP.DYN.LE00.IN',
    'health_expenditure': 'SH.XPD.CHEX.PC.CD',
    'sanitation': 'SH.STA.BASS.ZS',
    'mortality_u5': 'SH.DYN.MORT',
    'pollution': 'EN.ATM.PM25.MC.M3',
    'obesity': 'SH.STA.OB18.ZS',
    'gdp_per_capita': 'NY.GDP.PCAP.CD'
}

def fetch_worldbank_data(indicator_code, year='2020', per_page=1000):
    url = f"http://api.worldbank.org/v2/country/all/indicator/{indicator_code}?format=json&per_page={per_page}&date={year}"
    print(f"Fetching: {indicator_code}")
    
    response = requests.get(url)
    if response.status_code != 200:
        print(f"Error fetching data for {indicator_code}")
        return pd.DataFrame()
    
    data = response.json()
    if not data or len(data) < 2:
        print(f"No data returned for {indicator_code}")
        return pd.DataFrame()

    records = []
    for entry in data[1]:
        if entry['value'] is not None:
            records.append({
                'country': entry['country']['value'],
                'country_code': entry['country']['id'],
                'indicator': entry['indicator']['id'],
                'indicator_name': entry['indicator']['value'],
                'year': entry['date'],
                'value': entry['value']
            })
    
    return pd.DataFrame(records)

raw_data_path = os.path.join("..", "data", "raw")
os.makedirs(raw_data_path, exist_ok=True)


for name, code in indicators.items():
    df = fetch_worldbank_data(code)
    if not df.empty:
        output_path = os.path.join(raw_data_path, f"{name}.csv")
        df.to_csv(output_path, index=False)
        print(f"Saved: {output_path}")
    else:
        print(f"Skipped: {name}")

print("Data fetching complete.")