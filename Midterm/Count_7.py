"""Problem 3
Write a recursive Python function, given a non-negative integer N, to count and return the number of occurrences of the digit 7 in N.

For example:
count7(717) -> 2
count7(1237123) -> 1
count7(8989) -> 0"""

def count7(N):
    '''
    N: a non-negative integer
    '''
    if N == 0:
        return 0
    if N % 10 == 7:
        return 1 + count7(N // 10)
    else:
        return 0 + count7(N // 10)  
        
val = int(input("Enter an integer: "))
print(count7(val))
