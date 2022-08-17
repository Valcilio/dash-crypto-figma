import datetime as dt
import pandas as pd

class PlotData():

    def __init__(self, df: pd.DataFrame, date_col: str = 'nan', **kwargs):

        self.df = df.copy()
        self.date_col = date_col

    def check_dateindex(self, **kwargs):
        '''Check if the index is datetimeindex'''

        df = self.df.copy()

        df['partner'] = 1
        df = df['partner'].reset_index(drop=False).select_dtypes('datetime64[ns]')
        date_index_check = df.shape[1]

        return date_index_check

    def transform_dateindex(self, date_index_check: int, **kwargs):
        '''Transform index to datetimeindex if it's not a datetimeindex yet using
        the column passed how date_col at the start of this class'''

        df = self.df.copy()

        if (self.date_col == 'nan') & (date_index_check == 0):
            ValueError('''Is necessary one date info in index or column to do time procedures!''')

        elif (self.date_col != 'nan') & (date_index_check == 0):
            df[self.date_col] = pd.to_datetime(df[self.date_col])
            df = df.set_index(self.date_col)    
        
        else:
            self.date_col = 'index'

        return df
    
    def check_transform_dateindex(self, **kwargs):
        '''Run check and transform datetimeindex methods to check if exist some datetime index
        and if not transform the date_col to a datetimeindex format'''

        date_index_check = self.check_dateindex()
        df = self.transform_dateindex(date_index_check = date_index_check)

        return df

    def derivate_time_info(self, **kwargs):
        '''Derivate time information from the datetimeindex'''
        
        df = self.check_transform_dateindex()

        df['Year'] = df.index.year
        df['Month'] = df.index.month
        df['Week of Year'] = df.index.isocalendar().week
        df['Day of Month'] = df.index.day
        df['Day of Week']  = df.index.day_of_week
        df['Daily'] = df.index

        cols = [['Week of Year', 'Weekly'], ['Month', 'Monthly']]
        
        for c in cols: 
            df[c[0]] = df[c[0]].astype(int).apply(lambda x: '0' + str(x) if x < 10 else str(x))
            df['Year'] = df['Year'].astype(str)
            df[c[1]] = df['Year'] + df[c[0]]

        df['Year']  = df['Year'].astype(int)
        df['Month'] = df['Month'].astype(int)
        df['Week of Year']  = df['Week of Year'].astype(int)

        df['Weekend'] = df['Day of Week'].apply(lambda x: 
                                                1 if x in [5, 6] else 0)

        return df

    def derivate_int_float_columns(self, **kwargs):
        '''Filter dataset to just contain int64 and float64 columns'''

        date_index_check = self.check_dateindex()

        if (self.date_col == 'nan') & (date_index_check == 0):
            df = self.df.copy()
        else:
            df = self.check_transform_dateindex()
        
        num_attributes = df.select_dtypes(include=['int64', 'float64'])

        return num_attributes