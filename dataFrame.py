import pandas as pd
import datetime

class DataFrame:
    def __init__(self,filename):
        self.df = pd.read_csv(filename)
        self.column_names = self.df.columns
        self.convert_dates()

    def convert_dates(self):
        dates = []
        for i in range(0, len(self.df)):
            dates.append(datetime.datetime(int(self.df.loc[i, "Year"]), int(self.df.loc[i, "Month"]), int(self.df.loc[i, "Day"]), int((self.df.loc[i, "Time"])[0:2]), int((self.df.loc[i, "Time"])[3:]) ))
        self.df['Datetime'] = dates

    def get_column(self, column):
        try:
            if column not in self.column_names:
                raise ValueError("Column not found in data")
        except ValueError as e:
            print(e)
        return self.df[column]

    def get_column_names(self):
        return self.column_names

    def filter_by_amount(self, amount):
        if amount == "":
            return self.df
        df = self.df[self.df['Amount'] == amount]
        return df

    def filter_by_year(self, year):
        if year == "":
            return self.df
        df = self.df[self.df['Year'] == year]
        return df

    def filter_by_month(self, month):
        if month == "":
            return self.df
        df = self.df[self.df['Month'] == month]
        return df

    def filter_by_day(self, day):
        if day == "":
            return self.df
        df = self.df[self.df['Day'] == day]
        return df

    def filter_by_time(self, time):
        if time == "":
            return self.df
        df = self.df[self.df['Time'] == time]
        return df

    def filter_by_source(self, source):
        if source == "":
            return self.df
        df = self.df[source.lower() in self.df['Source'].str.lower()]
        return df

    def filter_by_category(self, category):
        if category == "":
            return self.df
        df = self.df[self.df['Category'].str.lower() == category.lower()]
        return df

    def merge_df(self, data_frames):
        sets = [set(map(tuple, df.values)) for df in data_frames]
        common_rows = set.intersection(*sets)
        filtered_frame = pd.DataFrame(list(common_rows), columns=self.column_names)
        return filtered_frame