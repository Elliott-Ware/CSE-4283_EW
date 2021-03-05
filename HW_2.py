from Retirement import Retirement
from BMI import BMI
x = input("What service would you like? ENTER 'B' for Body Mass Index calculator or 'S' for Retirement for Savings Calculator. ")
x2 = x.capitalize()

if x2 == 'S' or x2 == 'B':
    if x2 == 'S':
        Retirement.retireFunc()

    if x2 == 'B':
        BMI.calculator()

else:
    print("Entered a wrong value! Please Try Again!")

