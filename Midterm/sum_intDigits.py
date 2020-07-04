"""Problem 6
Write a recursive Python function, given a non-negative integer N, to calculate and return the sum of its digits."""

def sumDigits(N):
    '''
    N: a non-negative integer
    '''
    if N == 0: 
        return 0
    return (N%10 + sumDigits(N // 10))
    
val = int(input("Enter an integer to count it's digits: "))
print(sumDigits(val))
