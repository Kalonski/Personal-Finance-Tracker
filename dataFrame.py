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
        df = self.df[self.df['Amount'] == int(amount)] #the inner statement returns a mask series of True/False values, the outer self.df[] returns rows where the condition is True
        return df

    def filter_by_year(self, year):
        if year == "":
            return self.df
        df = self.df[self.df['Year'] == int(year)]
        return df

    def filter_by_month(self, month):
        if month == "":
            return self.df
        df = self.df[self.df['Month'] == int(month)]
        return df

    def filter_by_day(self, day):
        if day == "":
            return self.df
        df = self.df[self.df['Day'] == int(day)]
        return df

    def filter_by_time(self, time):
        if time == "":
            return self.df
        df = self.df[self.df['Time'] == time]
        return df

    def filter_by_source(self, source):
        if source == "":
            return self.df
        df = self.df[self.df['Source'].str.lower().str.contains(source.lower(), na=False)]
        return df #This works similarly but instead returns True/False values dependent if the input string is in the row's string

    def filter_by_category(self, category):
        if category == "":
            return self.df
        df = self.df[self.df['Category'].str.lower() == category.lower()]
        return df

    def merge_df(self, data_frames):
        frame1 = data_frames[0]
        for i in range(1, len(data_frames)):
            frame1 = pd.merge(frame1, data_frames[i], on=["Amount", "Year", "Month", "Day", "Time", "Source", "Category","Datetime"], how="inner")
        return frame1

        #ets = [set(map(tuple, df.values)) for df in data_frames]
        #common_rows = set.intersection(*sets)
        #filtered_frame = pd.DataFrame(list(common_rows), columns=self.column_names)
        #return filtered_frame
