import pandas as pd
import wbgapi as wb
from config import selected_indicators

def fetch_and_transform():
    data = []
    
    for row in wb.data.fetch(selected_indicators, mrnev=1):
        data.append(row)

    df = pd.DataFrame(data)

    # Convert 'YR2011' to 2011
    df['time'] = df['time'].apply(lambda x: int(x[2:]))
    
    # Drop aggregate column
    df.drop(columns=['aggregate'], inplace=True)
    
    # Rename columns
    df.rename(columns={'time': 'year', 
                       "Series Code": "indicator_id", 
                       "Country Code": "country_code"}, 
              inplace=True)
    
    return df
