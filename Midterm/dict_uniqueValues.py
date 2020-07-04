"""Problem 5
Write a Python function that returns a list of keys in aDict that map to integer values that are unique (i.e. values appear exactly once in aDict). 
The list of keys you return should be sorted in increasing order. (If aDict does not contain any unique values, you should return an empty list.)"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    value_list = []
    key_list = []
    for value in aDict.values():
        value_list.append(value)
    for key, value in aDict.items():
        if value_list.count(value) == 1:
            key_list.append(key)
    return key_list
    
print(uniqueValues({1: 1, 2: 1, 3: 3}))
