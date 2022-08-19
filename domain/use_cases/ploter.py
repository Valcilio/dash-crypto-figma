import pandas as pd
import plotly.express as px
import streamlit as st

from domain.entities.plotdata import PlotData

class Ploter():

    def daily_stability(self, df: pd.DataFrame, **kwargs):
        '''Line pot with daily values'''

        cols_list = self._get_cols_list(df=df)
        fig = px.line(
                    df, 
                    x=cols_list[0], 
                    y=[cols_list[1], cols_list[2]], 
                    title="Cryptocurrency's Daily Stability"
                    )

        st.plotly_chart(fig)

    def monthly_stability(self, df: pd.DataFrame, **kwargs):
        '''Line plot with year-month values'''

        cols_list = self._get_cols_list(df=df)
        df = self._derivate_time_info(df=df, group_col='Monthly', keep_cols=[cols_list[1], cols_list[2]])
        fig = px.line(
                    df, 
                    x='Monthly', 
                    y=[cols_list[1], cols_list[2]], 
                    title="Cryptocurrency's Monthly Stability"
                    )

        st.plotly_chart(fig)

    def month_outlier_detector(self, df: pd.DataFrame, **kwargs):
        '''Boxplot plot with month values'''

        cols_list = self._get_cols_list(df=df)
        df = self._derivate_time_info(df=df, group_col='Month', keep_cols=[cols_list[1], cols_list[2]])
        fig = px.box(
                    df, 
                    x='Month', 
                    y=[cols_list[1], cols_list[2]], 
                    title="Outlier Detector to Month"
                    )

        st.plotly_chart(fig)

    def distribution(self, df: pd.DataFrame, **kwargs):
        '''Boxplot plot with month values'''

        cols_list = self._get_cols_list(df=df)
        fig = px.histogram(
                        df, 
                        x=cols_list[1], 
                        title="Distribution of the Cryptocurrency"
                        )

        st.plotly_chart(fig)

    def _derivate_time_info(self, df: pd.DataFrame, group_col: str, keep_cols: list, **kwargs):
        '''Derivate time info to create plots'''

        df_full = PlotData(df=df, date_col='timestamp').derivate_time_info()
        keep_cols.append(group_col)
        df = df_full[keep_cols].groupby(group_col).median().reset_index()

        return df

    def _get_cols_list(self, df: pd.DataFrame, **kwargs):
        '''Get the list of cols from the dataframe'''

        return list(df.columns)