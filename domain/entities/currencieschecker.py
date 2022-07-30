import pandas as pd

class CurrenciesChecker():

    def __init__(self, df: pd.DataFrame, column: str, next_days: int, **kwargs):

        self.df = df
        self.column = column
        self.next_days = next_days

    def check_columns_no_model(self, **kwargs):
        '''Check the columns returned without model data in API'''

        test_cols_list = ['timestamp', self.column]
        cols_list = list(self.df.columns)

        assert test_cols_list == cols_list

    def check_columns_with_model(self, **kwargs):
        '''Check the columns returned with model data in API'''

        test_cols_list = ['timestamp', self.column, self.column + '_forecast']
        cols_list = list(self.df.columns)

        assert test_cols_list == cols_list

    def check_quantity_rows_no_model(self, **kwargs):
        '''Check if the quantity of rows are returning 
        correctly without model data in API'''

        assert self.df.shape[0] == 1000

    def check_quantity_rows_with_model(self, **kwargs):
        '''Check if the quantity of rows are returning 
        correctly without model data in API'''

        assert self.df.shape[0] == (1000 + self.next_days + 1)