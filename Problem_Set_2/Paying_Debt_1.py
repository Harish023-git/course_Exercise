"""Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

monthlyPaymentRate - minimum monthly payment rate as a decimal

Monthly interest rate= (Annual interest rate) / 12.0
Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)"""


balance = int(input("Enter Balance: "))
annualInterestRate = float(input("Enter Annual Intrest rate: "))
monthlyPaymentRate = float(input("Enter Montly Payment Rate: "))

for i in range(12):
    balance = ((annualInterestRate/12.0) * (balance - (balance * monthlyPaymentRate))) + balance - (balance * monthlyPaymentRate)
    
print("Remaining balance:", round(balance, 2)) 
