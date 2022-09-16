import os
import pandas as pd
import streamlit as st

from domain.connectors.apresentator import Apresentator
from domain.connectors.datagetter import DataGetter

datagetter = DataGetter()

def header():
    '''Header of the dashboard'''

    return st.header("Cryptocurrencies' Analysis")

def run_questions():
    '''Call all question to get data from user'''

    datagetter.run_all_questions()

@st.cache(suppress_st_warning=True)
def request_data():
    '''Button to request data'''

    if st.button('Update Data'):
        df = datagetter.request_data()
    
    return df

def plots(df: pd.DataFrame):
    '''Plot all figures'''

    Apresentator(df).plot_all()

def download_button(df: pd.DataFrame):
    '''Enable downloading the dataset'''

    return DataGetter().download_button(df)

if __name__ == '__main__':
    st.write(os.environ.get('FIGMA_CRYPTO_API_URL'))
    header()
    run_questions()

    try:
        df = request_data()
    except:
        df = None

    if df is None:
        pass
    else:
        download_button(df)
        plots(df)