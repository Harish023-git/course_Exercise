"""Now write a program that calculates the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months. By a fixed monthly payment, we mean a single number which does not change each month, but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:

balance - the outstanding balance on the credit card

annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment that will pay off all debt in under 1 year"""

def debt(balance, annualInterestRate):
    monthlyPaymentRate = 0
    init_balance = balance
    Monthly_interest_rate = annualInterestRate/12
    while balance > 0:
        for i in range(12):
            balance = balance - monthlyPaymentRate + ((balance - monthlyPaymentRate) * Monthly_interest_rate)
        
        if balance > 0:
            monthlyPaymentRate += 10
            balance = init_balance
        elif balance <= 0:
            break
    return monthlyPaymentRate
        
balance = int(input("Enter the Balance: "))
annualInterestRate = float(input("Enter the Annual Interest Rate: "))
print('Lowest Payment:', debt(balance, annualInterestRate))
