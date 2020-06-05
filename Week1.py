''' Problem 1:
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
For example, if s = 'azcbobobegghakl', your program should print:
Number of vowels: 5 '''

s = s.lower()
vowels = ('a','e','i','o','u')
count = 0
for i in range(len(s)):
    if s[i] in vowels:
        count += 1
print('Number of vowels:',count)

''' Problem 2:
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2 '''

count = 0
for i, v in enumerate(s):
    if s[i:i+3] == 'bob': 
        count += 1
print('Number of times bob occurs is:',count)

''' Problem 3:
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh '''

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
