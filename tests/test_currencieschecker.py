import os
import pandas as pd
import json
import requests

from domain.entities.currencieschecker import CurrenciesChecker

def get_test_data(crypto, market_curr, column, old_days, next_days, run_model):
    '''Get data for testing the dash from the backend'''

    url = os.environ.get('FIGMA_CRYPTO_API_URL')
    header = {'Content-type': 'application/json' }
    framework_data = {'crypto': crypto, 
                    'market_curr': market_curr, 
                    'run_model': run_model,
                    'column': column,
                    'old_days': old_days,
                    'next_days': next_days}

    framework_json = json.dumps(framework_data)
    r = requests.post(url, data=framework_json, headers=header)
    df = pd.DataFrame(r.json(), columns=r.json()[0].keys())

    return df

crypto = 'ETH'
market_curr = 'BRL'
column = 'low'
old_days = 0
next_days = 14

# calling functions
df_no_model = get_test_data(crypto, market_curr, column, old_days, next_days, run_model=False)
df_with_model = get_test_data(crypto, market_curr, column, old_days, next_days, run_model=True)

def test_check_columns_no_model():
    '''Test the columns returned without model data in API'''

    check_currencies = CurrenciesChecker(df=df_no_model, column=column, next_days=next_days)
    check_currencies.check_columns_no_model()
    
def test_check_columns_with_model():
    '''Test the columns returned with model data in API'''

    check_currencies = CurrenciesChecker(df=df_with_model, column=column, next_days=next_days)
    check_currencies.check_columns_with_model()

def test_check_quantity_rows_no_model():
    '''Test if the quantity of rows are returning 
    correctly without model data in API'''

    check_currencies = CurrenciesChecker(df=df_no_model, column=column, next_days=next_days)
    check_currencies.check_quantity_rows_no_model()

def test_check_quantity_rows_with_model():
    '''Test if the quantity of rows are returning 
    correctly without model data in API'''

    check_currencies = CurrenciesChecker(df=df_with_model, column=column, next_days=next_days)
    check_currencies.check_quantity_rows_with_model()
