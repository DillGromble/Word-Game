

import random


VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    """
    print("Loading word list from file...")
    
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = []
    
    for line in inFile:
        wordList.append(line.strip().lower())
        
    print("  ", len(wordList), "words loaded.")
    return wordList




def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.
    """
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	


def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.
    """
    score = 0
    
    for char in word:
        score += SCRABBLE_LETTER_VALUES[char]
        
    score *= len(word)
    
    if len(word) == n:
        score += 50
    return score




def displayHand(hand):
    """
    Displays the letters currently in the hand.
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter,end=" ")       
    print()                             




def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.
    """
    hand={}
    numVowels = n // 3
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand




def updateHand(hand, word):

    new = hand.copy() 
    
    for char in word:
        new[char] = new[char] - 1
           
    return new




def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.
    """
    test = True
    tempHand = hand.copy()
    
    for char in word:
        if (char not in tempHand.keys()) or (tempHand[char] == 0):
            test = False
            break
        tempHand[char] -= 1
        
    if word not in wordList:
        test = False
        
    return test




def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    """
    return sum(hand.values())




def playHand(hand, wordList, n):
    
    totalScore = 0
    
    while len(hand) > 1:
        
        print("Current Hand: ", end=' ')
        
        displayHand(hand)
        
        wordTry = input('Enter word, or a "." to indicate that you are finished: ')
        
        if wordTry == '.':
            break

        else:
            if not isValidWord(wordTry, hand, wordList):
                print("Invalid word, please try again.\n\n")
            
            else:
                score = getWordScore(wordTry, n)
                totalScore += score
                print('"{}" earned {} points!  You now have {} points.\n'.format(wordTry, score, totalScore))
                
                hand = updateHand(hand, wordTry)

                if sum(hand.values()) == 0:
                    print("Run out of letters. Total score: {} points.".format(totalScore))
                    return

    print("Game over!  Your total score was: {}".format(totalScore))

