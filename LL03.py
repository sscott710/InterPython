'''Module name: LL03.py
Author: Savannah Scott
Last Date Modified: 2/5/2021

Purpose of this module: This module provides a simple script
that allows the user to calculate the total cost of an eating-out.
The total cost consists of the billing dollar of the meal, the amount
of tax paid, and the tip. This was me trying the problem on my own. It might be
wrong lol. 
'''#problem 1
#enter user's info
#not sure if it was user inputed or already in the variables
salesTaxRate = float(input("Enter the sales tax rate: "))
tipRate = float(input("Enter the percentage you want to tip: "))
date= str(input("Enter date of meal: "))
time = str(input("Enter time of meal: "))
costOfMeal = float(input("Enter the cost of the meal: "))
#if not user-inputted
'''salesTaxRate = float(12.6)
tipRate = float(20.0)
date= str("January 31st")
time = str("12:00")
costOfMeal = float("35.00")'''
print()
#calculate
amountSalesTax = round((costOfMeal * (salesTaxRate/100.00)), 2)
amountTip = round((costOfMeal * (tipRate/100.00)), 2)
totalCost = amountSalesTax + amountTip + costOfMeal
#print out info
print("Date: " + date + " Time: " + time)
print("Sales Tax Rate: "+ str(salesTaxRate) + "%")
print("Amount for sales tax: $" + str(amountSalesTax));
print("Tip Rate: " + str(tipRate) + "%")
print("Amount for the tip: $" + str(amountTip))
print("Cost of Meal: $ " + str(costOfMeal))
print("Total amount paid: $" + str(totalCost))
                     
