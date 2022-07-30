from datetime import datetime
import pandas as pd
import plotly.express as px
import streamlit as st

class StreamlitApp():

    def __init__(self, **kwargs):

        df = pd.read_csv('/home/valcilio/all_proj/figma_assus/dash-crypto-figma/tests/test_data/test_df.csv')
        df = df.drop('Unnamed: 0', axis=1)
        self.df = df

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

    def filter_slider(self, slider_min_value, slider_max_value, slider_default_value, **kwargs):
        '''Develop slider filter for streamlit'''

        slider_value = st.slider('test filter', 
                                min_value=slider_min_value,
                                max_value=slider_max_value, 
                                value=slider_default_value,
                                format="MM/DD/YY")

        return slider_value

    def st_app(self, **kwargs):
        
        min_datetime = self._min_datetime()
        max_datetime = self._max_datetime()
        slider_datetime = self.filter_slider(min_datetime, max_datetime, min_datetime)


        self.df['timestamp'] = pd.to_datetime(self.df['timestamp'])
        df_plot = self.df[self.df['timestamp'] >= slider_datetime]

        fig = px.line(df_plot, x='timestamp', y=['low', 'low_forecast'], title="Cryptocurrency's Values")
        st.plotly_chart(fig)
        
if __name__ == '__main__':
    StreamlitApp().st_app()