''' Problem 1: Implement the function isWordGuessed that takes in two parameters - a string, secretWord, and a list of letters, 
lettersGuessed. This function returns a boolean - True if secretWord has been guessed (ie, all the letters of secretWord 
are in lettersGuessed) and False otherwise.'''

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in secretWord:
        if i in lettersGuessed:
            result = True
        else:
            result = False
            break
    return result
    
secretWord = input('Enter the secretWord: ')
lettersGuessed = input('Enter the letters guessed: ')
print(isWordGuessed(secretWord, lettersGuessed))  
