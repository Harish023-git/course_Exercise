balance = int(input("Enter Balance: "))
annualInterestRate = float(input("Enter Annual Intrest rate: "))
monthlyPaymentRate = float(input("Enter Montly Payment Rate: "))

for i in range(12):
    balance = ((annualInterestRate/12.0) * (balance - (balance * monthlyPaymentRate))) + balance - (balance * monthlyPaymentRate)
    
print("Remaining balance:", round(balance, 2)) 
