from dataFrame import DataFrame
import pandas as pd

class IncomeFrame(DataFrame):
    def __init__(self,filename):
        super().__init__(filename)
        self.total_income = 0


    def get_total_income(self):
        self.total_income = sum(self.df['Amount'])
        return self.total_income


