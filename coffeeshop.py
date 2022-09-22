#COFFEE SHOP PROGRAM
# - Concepts: print, input, variable use, datatype casting

#PSEUDO-CODE 
# 1 - Welcome message
from typing import final


print("Welcome to Damon's Coffee Shop!")

# 2 - Instructions to user
print("This is a program to calculate your order total.")
print("All you have to do is enter how many cups of coffee you want!")
print("Coffee comes in one (1) size only, for LOW LOW price of $1.55!!!!! wow!")

# 3 - Assign values to required variables
price = 1.50 #defined price for single cup
subtotal = 0.0 #Variable initialization
taxrate = 0.15 #Tax applied after purchase
taxamount = 0.0 
grandtotal = 0.0

# 4 - Input - How many cups?
numofcups = input("How many cups would you like?") #testvalue = 3

# 4a - Whoops! Change string 3 to number 3!
convertednumofcups = int(numofcups)

# 5 - Calculate : (cups * price)
subtotal = convertednumofcups * price

# 5A - Calculate Tax
taxamount = subtotal * taxrate

# 5B - Grand Total
grandtotal = subtotal + taxamount

# 6 - Display calculated total to user
print("You bought {0} cups of coffee, for {1:.2f} each for a subtotal of ${2:.2f}".format(numofcups, price, subtotal))
print("Your tax amount is ${0:.2f} and your grand total is ${1:.2f}." .format(taxamount, grandtotal))

# 7 - End program/thank you msg, recipt?
print("Thank you for stopping by Damon's Coffee Shop. Have a great day!")