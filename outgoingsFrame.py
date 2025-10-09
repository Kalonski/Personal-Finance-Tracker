from dataFrame import DataFrame
import pandas as pd

class OutgoingsFrame(DataFrame):
    def __init__(self,filename):
        super().__init__(filename)
        self.total_outgoings = 0


    def get_total_outgoings(self):
        self.total_outgoings = sum(self.df['Amount'])
        return self.total_outgoings
