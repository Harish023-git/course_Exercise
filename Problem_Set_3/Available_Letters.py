''' Problem 3: implement the function getAvailableLetters that takes in one parameter - a list of letters, lettersGuessed. 
This function returns a string that is comprised of lowercase English letters - all lowercase English letters that are not in 
lettersGuessed.'''

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for i in lettersGuessed:
        if i in alphabets:
            alphabets.remove(i)
    return ''.join(alphabets)

lettersGuessed = input('Enter the letters guessed: ')    
print(getAvailableLetters(lettersGuessed))
