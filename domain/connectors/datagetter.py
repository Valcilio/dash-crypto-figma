import os
import pandas as pd
import json
import requests
import streamlit as st

from domain.use_cases.questioner import Questioner

class DataGetter():

    def __init__(self):

        self.url = os.environ.get('FIGMA_CRYPTO_API_URL')
        self.questioner = Questioner()

    def request_data(self):
        '''Make a call on API to get the data'''

        r = requests.post(self.url, data=self._framework_data(), headers=self._header())
        
        return pd.DataFrame(r.json(), columns=r.json()[0].keys())

    def run_all_questions(self):
        '''Run all question to get the data for predict'''

        self.questioner.subheader()
        self.market_curr = self.questioner.market_curr()
        self.crypto_curr = self.questioner.crypto_curr()
        self.info_analy = self.questioner.info_extract()
        self.forecast_days = self.questioner.forecasting_quantity_days()

    def download_button(self, df: pd.DataFrame):
        '''Plot download button to '''

        st.download_button(
            label="Download Data as CSV",
            data=self._convert_df(df),
            file_name='cryptocurrency.csv',
            mime='text/csv',
        )

    def _framework_data(self):
        '''Dict with framework data informations'''

        self._treat_forecast_days_error()
        framework_data = {'crypto': self.crypto_curr, 
                        'market_curr': self.market_curr, 
                        'run_model': True,
                        'column': self.info_analy,
                        'old_days': 0,
                        'next_days': self.forecast_days}

        framework_json = json.dumps(framework_data)

        return framework_json

    def _treat_forecast_days_error(self):
        '''Treating forecast days'''

        try:
            self.forecast_days = self.forecast_days
        except:
            self.forecast_days = 1

    def _header(self):
        '''Return the header to make requests in the API'''

        return {'Content-type': 'application/json' }

    @st.cache
    def _convert_df(self, df: pd.DataFrame):
        '''Save dataframe as csv'''

        return df.to_csv()