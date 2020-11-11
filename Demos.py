# This program demonstrates how a floating-point
# number is displayed with no formatting and with formatting.
#this is a change from the desktop version of my file
amountDue = 23000.0
monthlyPayment = amountDue / 12
print("The monthly payment is", (format(monthlyPayment, ',.2f')))



print(format(monthlyPayment, ',.2f'))

print(format(0.5, '%'))

print(format(0.5, ".02%"))

print(format(123456, '10,d'))

