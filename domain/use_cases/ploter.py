import pandas as pd
import plotly.express as px
import streamlit as st

from domain.entities.plotdata import PlotData

class Ploter():

    def daily_stability(self, df: pd.DataFrame, **kwargs):

        cols_list = self._get_cols_list(df=df)
        fig = px.line(
                    df, 
                    x=cols_list[0], 
                    y=[cols_list[1], cols_list[2]], 
                    title="Cryptocurrency's Daily Stability"
                    )

        st.plotly_chart(fig)

    def monthly_stability(self, df: pd.DataFrame, **kwargs):

        cols_list = self._get_cols_list(df=df)
        df = self._derivate_time_info(df=df, group_col='Monthly', keep_cols=[cols_list[1], cols_list[2]])
        fig = px.line(
                    df, 
                    x='Monthly', 
                    y=[cols_list[1], cols_list[2]], 
                    title="Cryptocurrency's Monthly Stability"
                    )

        st.plotly_chart(fig)

    def _derivate_time_info(self, df: pd.DataFrame, group_col: str, keep_cols: list, **kwargs):

        df_full = PlotData(df=df, date_col='timestamp').derivate_time_info()
        keep_cols.append(group_col)
        df = df_full[keep_cols].groupby(group_col).median().reset_index()

        return df

    def _groupby_data(self, df: pd.DataFrame, **kwargs):
        return df.groupby(x='timestamp', )

    def _get_cols_list(self, df: pd.DataFrame, **kwargs):
        return list(df.columns)