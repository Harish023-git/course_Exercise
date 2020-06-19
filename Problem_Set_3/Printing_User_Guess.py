''' Problem 2: Implement the function getGuessedWord that takes in two parameters - a string, secretWord, and a list of 
letters, lettersGuessed. This function returns a string that is comprised of letters and underscores, based on what letters 
in lettersGuessed are in secretWord.'''

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    result = []
    for i in secretWord:
        if i in lettersGuessed:
            result.append(i)
        else:
            result.append('_')
    return ''.join(result)
    
secretWord = input('Enter the secret word: ')
lettersGuessed = input('Enter the letters gussed: ')
print(getGuessedWord(secretWord, lettersGuessed))
