import pandas as pd
from matplotlib import pyplot as plt

class StabilityPloter():

    def __init__(self, df: pd.DataFrame, **kwargs):

        self.df = df