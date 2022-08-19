import pandas as pd
import streamlit as st

from domain.connectors.apresentator import Apresentator
from domain.connectors.datagetter import DataGetter

class StreamlitApp():

    def __init__(self):

        self.datagetter = DataGetter()

    def streamlit_app(self):
        '''Run Streamlit APP'''

        self.datagetter.run_all_questions()

        if st.button('Show Dashboard'):
            df = self.datagetter.request_data()
            Apresentator(df=df).plot_all()

if __name__ == '__main__':
    StreamlitApp().streamlit_app()