# Hangman game

import random

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

wordlist = loadWords()

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

def hangman(secretWord):
    '''
    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.
    '''
    print('Welcome to the game, Hangman!')
    print('I am thinking of a word that is {} letters long.'.format(len(secretWord)))
    mistakesMade = 0
    lettersGuessed = []
    while mistakesMade <8:
        print('------------')
        print('You have {} guesses left.'.format(8-mistakesMade))
        print('Available letters:',getAvailableLetters(lettersGuessed))
        letter = input('Please guess a letter: ')
        if letter in lettersGuessed:
            lettersGuessed += letter
            print("Oops! You've already guessed that letter:",getGuessedWord(secretWord, lettersGuessed))
        elif letter in secretWord:
            lettersGuessed += letter
            print('Good guess:',getGuessedWord(secretWord, lettersGuessed))
        elif letter not in secretWord:
            lettersGuessed += letter
            print('Oops! That letter is not in my word:',getGuessedWord(secretWord, lettersGuessed))
            mistakesMade += 1
        if isWordGuessed(secretWord, lettersGuessed):
            print('------------')
            print('Congratulations, you won!')
            break
    if mistakesMade > 7:
        print('------------')
        print('Sorry, you ran out of guesses. The word was {}.'.format(secretWord))
        
hangman(chooseWord(wordlist))
