from ps4a import *

import time




def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives
    the maximum value score, and return it.
    """
    bestScore = 0
    bestWord = None
    
    for word in wordList:       
        if isValidWord(word, hand, wordList):        
            score = getWordScore(word, n)           
            
            if (score > bestScore):
                bestScore = score
                bestWord = word  
    return bestWord




def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer
    chooses it.
    """
    
    totalScore = 0
    
    while (calculateHandlen(hand) > 0) :
        
        print("Current Hand: ", end=' ')
        displayHand(hand)
        
        word = compChooseWord(hand, wordList, n)
        
        if word == None:
            break
        
        else :
            if (not isValidWord(word, hand, wordList)) :
                print('This is a terrible error! I need to check my own code!')
                break
            else :
                score = getWordScore(word, n)
                totalScore += score
                print('"' + word + '" earned ' + str(score) + ' points. Total: ' + str(totalScore) + ' points')
                
                hand = updateHand(hand, word)
                print()

    print('Total score: ' + str(totalScore) + ' points.')




def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
    """
    inputs = [['n', 'r', 'e'], ['u', 'c']]
    hand = ''

    while True:
        inp = ''
    
        while inp not in inputs[0]:
            inp = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
    
            user = ''
            while (user not in inputs[1]) and (inp.lower() != 'e') and (inp in inputs[0]):
                if inp.lower() == 'r' and hand == '': break
                user = input("Enter u to have yourself play, c to have the computer play: ")
                if user.lower() == 'c':
                    player = 'comp'
                elif user.lower() == 'u':
                    player = 'user'
                else:
                    print("Invalid command.")
    
    
            if inp.lower() == 'n':
                hand = dealHand(HAND_SIZE)
                if player == 'user':
                    playHand(hand, wordList, HAND_SIZE)
                else:
                    compPlayHand(hand, wordList, HAND_SIZE)
            
            elif inp.lower() == 'r':
                if hand == '':
                    print("You have not played a hand yet. Please play a new hand first!")
                    inp = ''
                    pass
                else:
                    if player == 'user':
                        playHand(hand, wordList, HAND_SIZE)
                    else:
                        compPlayHand(hand, wordList, HAND_SIZE)
                    
            
            elif inp.lower() == 'e':
                return
            
            else:
                print("Invalid command.")




if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)

