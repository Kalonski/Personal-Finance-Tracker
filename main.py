from incomeFrame import IncomeFrame

incomeFrame = IncomeFrame()

while True:
    ans1 = input("Would you like to see the total income?")
    if ans1.lower() == 'y':
        print("Total: ", incomeFrame.get_total_income())
    ans2 = input("Enter a column to search by")
    print(incomeFrame.get_column(ans2))
