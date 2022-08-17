from datetime import datetime
import pandas as pd
import streamlit as st

class Filter():

    def __init__(self, df: pd.DataFrame, **kwargs):

        self.df = df

    def filter_df_datetime(self, slider_datetime, **kwargs):
        '''Filter dataframe by slider datetime return'''

        df = self.df.copy()
        df['timestamp'] = pd.to_datetime(df['timestamp'])
        df_plot = df[df['timestamp'] >= slider_datetime]

        return df_plot

    def filter_slider_datetime(self, name: str, default_value: datetime = False, **kwargs):
        '''Develop slider filter for streamlit'''

        min_datetime = self._min_datetime()
        max_datetime = self._max_datetime()

        if default_value == False:
            default_value = min_datetime

        slider_value = st.slider(name, 
                                min_value=min_datetime,
                                max_value=max_datetime, 
                                value=default_value,
                                format="MM/DD/YY")

        return slider_value

    def _min_datetime(self, **kwargs):
        '''Get min datetime values'''

        date_year = int(self.df['timestamp'].min()[0:4])
        date_month = int(self.df['timestamp'].min()[5:7])
        date_day = int(self.df['timestamp'].min()[8:10])

        datetime_min = datetime(date_year, date_month, date_day)

        return datetime_min

    def _max_datetime(self, **kwargs):
        '''Get max datetime values'''

        date_year = int(self.df['timestamp'].max()[0:4])
        date_month = int(self.df['timestamp'].max()[5:7])
        date_day = int(self.df['timestamp'].max()[8:10])

        datetime_max = datetime(date_year, date_month, date_day)

        return datetime_max