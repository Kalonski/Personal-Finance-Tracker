from incomeFrame import IncomeFrame
from outgoingsFrame import OutgoingsFrame
import datetime


def total_balance(earnings, spending):
    # Input validation here----------------------------------------
    return earnings - spending

def total_amount_timeframe(df, startDate, endDate):
    # Input validation here----------------------------------------
    income = 0
    for i in range(0, len(df)):
        if startDate <= df.loc[i, "Datetime"] <= endDate:
            income += df.loc[i, "Amount"]
    return income





def get_dates_input():
    year = int(input("Enter a start year: "))
    month = int(input("Enter a start month: "))
    day = int(input("Enter a start day: "))
    time = input("Enter a start time: ")
    startDate = datetime.datetime(year, month, day, int(time[0:2]), int(time[3:5]))

    year = int(input("Enter an end year: "))
    month = int(input("Enter an end month: "))
    day = int(input("Enter an end day: "))
    time = input("Enter an end time: ")
    endDate = datetime.datetime(year, month, day, int(time[0:2]), int(time[3:5]))
    return startDate, endDate