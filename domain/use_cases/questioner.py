import streamlit as st

class Questioner():

    def create_dashboard(self):
        '''Button to start dashboard's creation'''

        return st.button('Show Dashboard')

    def crypto_curr(self):
        '''Select crypto currency for get data'''

        crypto_curr_selected = st.selectbox('Cryptocurrency', self._crypto_curr_options())
        crypto_curr = self._translated_crypto_curr().get(crypto_curr_selected)

        return crypto_curr

    def market_curr(self):
        '''Select makert currency for get data'''

        market_curr_selected = st.selectbox('Market Currency', self._market_curr_options())
        market_curr = self._translated_market_curr().get(market_curr_selected)

        return market_curr

    def info_extract(self):
        '''Info to use from dataframe'''

        return st.selectbox('Information to Analysis', self._informations())

    def make_forecast(self):
        '''Definy if the model is going to run or not'''

        make_forecast_selected = st.selectbox('Make forecasting', ['yes', 'no'])
        make_forecast = self._translated_make_forecast().get(make_forecast_selected)

        return make_forecast

    def forecasting_quantity_days(self):
        '''Number of days to be forecasting from the model'''

        forecast_days = st.number_input('Forecasting Days', 1)

        return forecast_days - 1

    def _translated_make_forecast(self):
        '''Translate make forecast'''

        return {'yes': True,
                'no': False}

    def _informations(self):
        '''List of informations to analysis'''

        return ['high', 
                'low', 
                'close', 
                'open', 
                'volume']

    def _translated_crypto_curr(self):
        '''Dictionary with market curr translated to initials'''

        return {'Bitcoin':'BTC', 
                'Ethereum':'ETH', 
                'Adacoin':'ADA', 
                'Dogecoin':'DOGE', 
                'Ripple':'XRP'}

    def _crypto_curr_options(self):
        '''List of market currencies who are accepted'''

        return ['Bitcoin', 
                'Ethereum', 
                'Adacoin', 
                'Dogecoin', 
                'Ripple']

    def _translated_market_curr(self):
        '''Dictionary with market curr translated to initials'''

        return {'American Dólar':'USD', 
                'Brazilian Real':'BRL', 
                'Chinese Yuan':'CNY', 
                'Euro':'EUR', 
                'British Pound Sterling':'GBP'}

    def _market_curr_options(self):
        '''List of market currencies who are accepted'''

        return ['American Dólar', 
                'Brazilian Real', 
                'Chinese Yuan', 
                'Euro', 
                'British Pound Sterling']