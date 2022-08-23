import pandas as pd
import streamlit as st

from domain.connectors.apresentator import Apresentator
from domain.connectors.datagetter import DataGetter

datagetter = DataGetter()

def run_questions():

    datagetter.run_all_questions()

@st.cache(suppress_st_warning=True)
def request_data():

    if st.button('Update Data'):
        df = datagetter.request_data()
    
    return df

def plots(df):

    if df is None:
        pass
    else:
        st.subheader("Cryptocurrency's Dashboard")
        Apresentator(df).plot_all()

if __name__ == '__main__':
    run_questions()

    try:
        df = request_data()
    except:
        df = None

    plots(df)