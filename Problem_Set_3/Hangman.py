''' Problem-4:
implement the function hangman, which takes one parameter - the secretWord the user is to guess. This starts up an 
interactive game of Hangman between the user and the computer. Be sure you take advantage of the three helper functions, 
isWordGuessed, getGuessedWord, and getAvailableLetters, that you've defined in the previous part.
There are four important pieces of information you may wish to store:
1. secretWord: The word to guess.
2. lettersGuessed: The letters that have been guessed so far.
4. mistakesMade: The number of incorrect guesses made so far.
5. availableLetters: The letters that may still be guessed. Every time a player guesses a letter, the guessed letter must 
be removed from availableLetters (and if they guess a letter that is not in availableLetters, you should print a message 
telling them they've already guessed that - so try again!). '''

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

    Follows the other limitations detailed in the problem write-up.
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
        
