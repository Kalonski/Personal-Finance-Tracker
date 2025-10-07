from numpy.f2py.auxfuncs import throw_error
from dataFrame import DataFrame
import pandas as pd

class IncomeFrame(DataFrame):
    def __init__(self):
        super().__init__()
        self.df = pd.read_csv('income.csv')
        self.columns = self.df.iloc[0].tolist()
        self.total_income = 0


    def get_total_income(self):
        self.total_income = sum(self.df['Amount'])
        return self.total_income

    def get_column(self, column):
        try:
            if column not in self.df.columns:
                raise ValueError("Column not found in data")
        except ValueError as e:
            print(e)
        return self.df[column]



