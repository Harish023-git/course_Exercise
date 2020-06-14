''' Problem 3:
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh '''

def check(s):
    longest = s[0]
    current = s[0]
    for c in s[1:]:
        if c >= current[-1]:
            current += c
            if len(current) > len(longest):
                longest = current
            else:
                current = c
    print("Longest substring in alphabetical order is:", longest)

s = input("Enter the string:")
check(s)
