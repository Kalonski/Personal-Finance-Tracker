import datetime

from incomeFrame import IncomeFrame
from outgoingsFrame import OutgoingsFrame
from maths import *

incomeFrame = IncomeFrame("income.csv")
outgoingsFrame = OutgoingsFrame("outgoings.csv")


while True: #I want to wake up, in a city that never sleeps
    choice = int(input("What operation is to be performed?\n"
                   "[1] - Print total income\n"
                   "[2] - Print total outgoings\n"
                   "[3] - Print total balance\n"
                   "[4] - Print total income over a time period\n"
                   "[5] - Print total outgoings over a time period\n"
                    "[6] - Print total balance over a time period\n"
                    "[7] - Print a column of a frame\n"
                    "[8] - Filter a dataframe\n"))
    match choice:
        case 1:
            print("Total income: ", incomeFrame.get_total_income())
        case 2:
            print("Total outgoings: ", outgoingsFrame.get_total_outgoings())
        case 3:
            print("Total balance: ",total_balance(incomeFrame.get_total_income(), outgoingsFrame.get_total_outgoings()))
        case 4:
            startDate, endDate = get_dates_input()
            print("Total income: ", total_amount_timeframe(incomeFrame.df, startDate, endDate))
        case 5:
            startDate, endDate = get_dates_input()
            print("Total outgoings: ", total_amount_timeframe(outgoingsFrame.df, startDate, endDate))
        case 6:
            startDate, endDate = get_dates_input()
            print("Total balance: ", total_balance(total_amount_timeframe(incomeFrame.df, startDate, endDate), total_amount_timeframe(outgoingsFrame.df, startDate, endDate)))
        case 7:
            frame = input("Which frame would you like to access? Income[i] | Outgoings[o]\n")
            column_name = input("Enter the name of the column you would like to display")
            if frame.lower() == "income" or frame.lower() == "i":
                print("Columns: ", incomeFrame.get_column_names())
                column_name = input("Enter the name of the column you would like to display")
                print(incomeFrame.get_column(column_name))
            if frame.lower() == "outgoings" or frame.lower() == "o":
                print("Columns: ", outgoingsFrame.get_column_names())
                column_name = input("Enter the name of the column you would like to display")
                print(outgoingsFrame.get_column(column_name))
        case 8:
            frame = input("Which frame would you like to access? Income[i] | Outgoings[o]\n")
            print("Enter values to filter by (Press ENTER to not filter by specific category)")
            amount = input("Amount:")
            year = input("Year:")
            month = input("Month:")
            day = input("Day:")
            time = input("Time:")
            source = input("Source:")
            category = input("Category:")
            if frame.lower() == "income" or frame.lower() == "i":
                print(incomeFrame.merge_df([incomeFrame.filter_by_amount(amount), incomeFrame.filter_by_year(year), incomeFrame.filter_by_month(month),
                                            incomeFrame.filter_by_day(day), incomeFrame.filter_by_time(time), incomeFrame.filter_by_source(source),
                                            incomeFrame.filter_by_category(category)]))




