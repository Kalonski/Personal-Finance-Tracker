import pandas as pd
import datetime

class DataFrame:
    def __init__(self,filename):
        self.df = pd.read_csv(filename)
        self.columns = self.df.iloc[0].tolist()
        self.convert_dates()

    def convert_dates(self):
        dates = []
        for i in range(0, len(self.df)):
            dates.append(datetime.datetime(int(self.df.loc[i, "Year"]), int(self.df.loc[i, "Month"]), int(self.df.loc[i, "Day"]), int((self.df.loc[i, "Time"])[0:2]), int((self.df.loc[i, "Time"])[3:]) ))
        self.df['Datetime'] = dates


    def get_column(self, column):
        try:
            if column not in self.df.columns:
                raise ValueError("Column not found in data")
        except ValueError as e:
            print(e)
        return self.df[column]