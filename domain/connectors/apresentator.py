from datetime import datetime
import pandas as pd
import streamlit as st

from domain.use_cases.filter import Filter
from domain.use_cases.ploter import Ploter

class Apresentator():

    def __init__(self, df: pd.DataFrame):

        self.df = df
        self.filter = Filter(df=self.df)
        self.ploter = Ploter()

    def plot_all(self):
        '''Run all methods of this aplication'''

        self.subheader()
        slider_default_datetime = self.default_filter()
        self.daily_lineplot(slider_default_datetime)
        self.monthly_lineplot(slider_default_datetime)
        self.histogram(slider_default_datetime)
        self.month_boxplot(slider_default_datetime)

    def subheader(self):
        '''Subheader indicating the start point of the dashboard'''

        return st.subheader("Cryptocurrency's Dashboard")

    def default_filter(self): 
        '''Create a default filter'''

        return self.filter.filter_slider_datetime(name='Default Dashboard Filters')

    def daily_lineplot(self, slider_default_datetime: datetime):
        '''Get the daily line plot with filter'''

        slider_value_datetime = self.filter.filter_slider_datetime(name='Filtering By Day', default_value=slider_default_datetime)
        df_plot = self.filter.filter_df_datetime(slider_value_datetime)
        self.ploter.daily_stability(df=df_plot)

    def monthly_lineplot(self, slider_default_datetime: datetime):
        '''Get the monthly line plot with filter'''

        slider_value_datetime = self.filter.filter_slider_datetime(name='Filtering Monthly', default_value=slider_default_datetime)
        df_plot = self.filter.filter_df_datetime(slider_value_datetime)
        self.ploter.monthly_stability(df=df_plot)

    def histogram(self, slider_default_datetime: datetime):
        '''Get the month boxplot plot with filter'''

        slider_value_datetime = self.filter.filter_slider_datetime(name='Filtering Distribution', default_value=slider_default_datetime)
        df_plot = self.filter.filter_df_datetime(slider_value_datetime)
        self.ploter.distribution(df=df_plot)

    def month_boxplot(self, slider_default_datetime: datetime):
        '''Get the month boxplot plot with filter'''

        slider_value_datetime = self.filter.filter_slider_datetime(name='Filtering Month', default_value=slider_default_datetime)
        df_plot = self.filter.filter_df_datetime(slider_value_datetime)
        self.ploter.month_outlier_detector(df=df_plot)
