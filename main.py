import pandas as pd
import streamlit as st

from domain.use_cases.filter import Filter
from domain.use_cases.ploter import Ploter

class StreamlitApp():

    def __init__(self, **kwargs):

        df = pd.read_csv('/home/valcilio/all_proj/figma_assus/dash-crypto-figma/tests/test_data/test_df.csv')
        df = df.drop('Unnamed: 0', axis=1)
        self.df = df
        self.filter = Filter(df=self.df)
        self.ploter = Ploter()

    def st_app(self, **kwargs):
        
        slider_default_datetime = self.filter.filter_slider_datetime(name='Default Dashboard Filters')

        slider_value_datetime = self.filter.filter_slider_datetime(name='Filtering Daily Dataframe', default_value=slider_default_datetime)
        df_plot = self.filter.filter_df_datetime(slider_value_datetime)

        self.ploter.daily_stability(df=df_plot)

        slider_value_datetime = self.filter.filter_slider_datetime(name='Filtering Monthly', default_value=slider_default_datetime)
        df_plot = self.filter.filter_df_datetime(slider_value_datetime)

        self.ploter.monthly_stability(df=df_plot)

if __name__ == '__main__':
    StreamlitApp().st_app()