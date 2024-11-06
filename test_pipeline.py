import pytest
import pandas as pd
from unittest.mock import patch, MagicMock 
from gender_api import fetch_and_transform
from database import save_to_sql

@patch('gender_api.wb.data.fetch') 
def test_fetch_and_transform_success(mock_fetch):  
    mock_fetch.return_value = [
        {'time': 'YR2011', 'series': 'SP.POP.TOTL', 'economy': 'USA', 'aggregate': None},
        {'time': 'YR2012', 'series': 'SP.ADO.TFRT', 'economy': 'USA', 'aggregate': None}
    ]

    df = fetch_and_transform()

    assert list(df.columns) == ['year', 'indicator_id', 'country_code']
    assert df.iloc[0]['year'] == 2011
    assert df.iloc[0]['indicator_id'] == 'SP.POP.TOTL'
    
    
@patch('database.create_engine')
def test_save_to_sql_success(mock_engine):
    mock_engine.return_value = MagicMock()
    
    df = pd.DataFrame({
        'indicator_id': ['SP.POP.TOTL'],
        'country_code': ['USA'],
        'year': [2021]
    })
    
    try:
        save_to_sql(dataframe_name=df, table_name="indicator_fact")
    except Exception:
        pytest.fail("save_to_sql raised an Exception!")
        

@patch('database.create_engine')
def test_save_to_sql_fail(mock_engine):
    mock_engine.side_effect = Exception("Database connection failure!")
    
    df = pd.DataFrame({
        'indicator_id': ['SP.POP.TOTL'],
        'country_code': ['USA'],
        'year': [2021]
    })
    
    with pytest.raises(Exception):
        save_to_sql(dataframe_name=df, table_name="indicator_fact")
