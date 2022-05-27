# IMPORTS
import os
import time as ti
from lazyme.string import color_print
import csv
import numpy as np
import random as rnd

# --------------------------------------------------------------------------------------------------------------------
# SETUP
# --------------------------------------------------------------------------------------------------------------------

def splitWord(word):
    return {char for char in word}

def removePossible():
    newPossiblewords = {}
    for wordNum in range(len(possibleWords)):

        deleted = False

        for letter in letters['wrong']:
            if deleted == False and letter in possibleWords[wordNum]: 
                deleted = True
                possibleWords.pop(wordNum)

        i = 0

        for correct in letters['correct']:
            if deleted == False:
                if correct != possibleWords[wordNum][i] and correct != '': 
                    deleted = True
                    possibleWords.pop(wordNum)
            i += 1

        i = 0                                 # 'missplaced': [['a','b','c'],[],[],[],[]]
        for y in letters['missplaced']:       # y = ['a','b','c']
            if deleted == False and y != []: 
                for z in y:                   # z = 'a'
                    if deleted == False: 
                        if z not in possibleWords[wordNum]:
                            deleted = True
                            possibleWords.pop(wordNum)
                        elif z == possibleWords[wordNum][i]:
                            deleted = True
                            possibleWords.pop(wordNum)
            i += 1
    x = 0
    for i in possibleWords:
        newPossiblewords[x] = possibleWords[i]
        x += 1
    return newPossiblewords

def removeAllowed():
    newAllowedWords = {}
    for wordNum in range(len(allowedWords)):
        wordArray = splitWord(allowedWords[wordNum])
        z = len(wordArray.intersection(letters['wrong']))
        if z > 3 : 
            allowedWords.pop(wordNum)
        elif allowedWords[wordNum] == guess:
            allowedWords.pop(wordNum)
    
    x = 0
    for i in allowedWords:
        newAllowedWords[x] = allowedWords[i]
        x += 1

    return newAllowedWords

def wordRemoval():

    if guess != wordle:
        
        newAllowed = removeAllowed()

        newPossible = removePossible()
        
            
        return newAllowed, newPossible

    return {0:wordle},{0:wordle}  

def wordlePicker():
    inWord = 0
    wordlelele = rnd.choice(list(possibleWords.values()))
    duplicates = False

    for x in range(5):
        for y in range(5):
            if wordlelele[x] in wordlelele[y]: inWord += 1
        if inWord > 1: duplicates = True
        inWord = 0

    if duplicates: 
        wordlelele = wordlePicker()
    
    return wordlelele

def correctChecker():
    # inWord = 0
    # duplicates = False

    # for x in range(5):
    #     for y in range(5):
    #         if wordle[x] in wordle[y]: inWord += 1
    #     if inWord > 2: duplicates = True
    #     inWord = 0

    for i in range(5):
        if wordle[i] == guess[i] : 
            letters['correct'][i] = guess[i]
            for x in range(5):
                if guess[i] in letters['missplaced'][x]: letters['missplaced'][x].remove(guess[i])
        elif guess[i] in wordle and guess[i] not in letters['missplaced'][i] and guess[i] not in letters['correct']: letters['missplaced'][i].append(guess[i])
        elif guess[i] not in wordle and guess[i] not in letters['wrong']: letters['wrong'].append(guess[i])

    if guess == wordle: return 6, True
    else: return t, False

def takeGuess(tries):
    guessCorrect = False
    while guessCorrect == False:
        newGuess = input("What's your next guess:  ").lower()
        if len(newGuess) == 5 and newGuess in allowedWords.values(): guessCorrect = True
        if newGuess == "p": 
            print(possibleWords)

    guesses[tries] = list(newGuess)

    return newGuess

def programGuessRemoval(testWordle, testGuess):
    testLetters = letters.copy()

    for i in range(5):
        if testWordle[i] == testGuess[i] : 
            testLetters['correct'][i] = testGuess[i]
            for x in range(5):
                if guess[i] in testLetters['missplaced'][x]: testLetters['missplaced'][x].remove(testGuess[i])
        elif testGuess[i] in testWordle and testGuess[i] not in testLetters['missplaced'][i] and testGuess[i] not in testLetters['correct']: testLetters['missplaced'][i].append(testGuess[i])
        elif testGuess[i] not in testWordle and testGuess[i] not in testLetters['wrong']: testLetters['wrong'].append(testGuess[i])
    
    return testLetters

def wordFiner():
    options = []
    wordsRemoved = 0
    newPossiblewords = {}
    xx = 0
    yy = 0 
    testLetters = letters
    
    for input in allowedWords.values():
        for answer in possibleWords.values():

            testLetters = programGuessRemoval(testLetters, answer, input)

            for wordNum in range(len(possibleWords)):

                deleted = False

                for letter in testLetters['wrong']:
                    if deleted == False and letter in possibleWords[wordNum]: 
                        deleted = True
                        wordsRemoved += 1

                i = 0

                for correct in testLetters['correct']:
                    if deleted == False:
                        if correct != possibleWords[wordNum][i] and correct != '': 
                            deleted = True
                            wordsRemoved += 1
                    i += 1

                i = 0                                 # 'missplaced': [['a','b','c'],[],[],[],[]]
                for y in testLetters['missplaced']:       # y = ['a','b','c']
                    if deleted == False and y != []: 
                        for z in y:                   # z = 'a'
                            if deleted == False: 
                                if z not in possibleWords[wordNum]:
                                    deleted = True
                                    wordsRemoved += 1
                                elif z == possibleWords[wordNum][i]:
                                    deleted = True
                                    wordsRemoved += 1
                    i += 1
            yy += 1
        xx += 1

winner = False
possibleWords = {}
allowedWords = {}
t = 0

letters = {'wrong': [],
           'correct': ['','','','',''],
           'missplaced': [[],[],[],[],[]]}     

guesses = [[' ', ' ', ' ', ' ', ' '], 
           [' ', ' ', ' ', ' ', ' '], 
           [' ', ' ', ' ', ' ', ' '], 
           [' ', ' ', ' ', ' ', ' '], 
           [' ', ' ', ' ', ' ', ' '], 
           [' ', ' ', ' ', ' ', ' ']]

with open('/Users/24nowak_p/Desktop/School/Programming/Programming Class/AdvancedProgramming/Python/Online Games/Wordle/txt/possibleWords.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        possibleWords[line_count] = row['word']
        line_count += 1

with open('/Users/24nowak_p/Desktop/School/Programming/Programming Class/AdvancedProgramming/Python/Online Games/Wordle/txt/allowedWords.csv', mode='r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    line_count = 0
    for row in csv_reader:
        allowedWords[line_count] = row['word']
        line_count += 1


# --------------------------------------------------------------------------------------------------------------------
# GAME
# --------------------------------------------------------------------------------------------------------------------

wordle = wordlePicker()

print(wordle)
ti.sleep(2)

while t < 6:

    os.system('clear')

    for i in letters:
        print(i, "    ", str(letters[i])[1:-1],"\n")

    color_print(" --------------- ", color='magenta')

    for wordPosition in range(6): # print all 6 words

        for letterPosition in range(5): # prints 1 word

            if letterPosition == 0 : 

                color_print("| ", color='magenta', end='')
                color_print(guesses[wordPosition][letterPosition].upper(), color='white', end='')

            elif letterPosition == 4:
                aa = "  " + guesses[wordPosition][letterPosition].upper()
                color_print(aa, color='white', end='')
                color_print(" |", color='magenta', end='\n')

            else:
                ab = "  " + guesses[wordPosition][letterPosition].upper()
                color_print(ab, color='white', end='')

        color_print(" --------------- ", color='magenta', end='\n')

    print("\n\n")

    guess = takeGuess(t)
    t, winner = correctChecker()
    allowedWords, possibleWords = wordRemoval()
    t += 1

    print(len(possibleWords))
    if len(possibleWords) < 5:
        for a in possibleWords.values():
            print(a)
        ti.sleep(3)




# --------------------------------------------------------------------------------------------------------------------
# FINAL DISPLAY
# --------------------------------------------------------------------------------------------------------------------




os.system('clear')
color_print(" --------------- ", color='magenta')

lastWord = 0

for i in range(6):
    if guesses[-1-i] == [' ', ' ', ' ', ' ', ' ']: lastWord = 6-(i+1)

for wordPosition in range(lastWord-1): # print all words, but the last one

    for letterPosition in range(5): # prints 1 word
        
        if letterPosition == 0 : 

            color_print("| ", color='magenta', end='')
            color_print(guesses[wordPosition][letterPosition].upper(), color='white', end='')

        elif letterPosition == 4:
            aa = "  " + guesses[wordPosition][letterPosition].upper()
            color_print(aa, color='white', end='')
            color_print(" |", color='magenta',)

        else:
            ab = "  " + guesses[wordPosition][letterPosition].upper()
            color_print(ab, color='white', end='')

    color_print(" --------------- ", color='magenta')
if winner: 
    for letterPosition in range(5): # prints 1 word
        
        if letterPosition == 0 : 

            color_print("| ", color='magenta', end='')
            color_print(guesses[lastWord-1][letterPosition].upper(), color='green', end='')

        elif letterPosition == 4:
            aa = "  " + guesses[lastWord-1][letterPosition].upper()
            color_print(aa, color='green', end='')
            color_print(" |", color='magenta',)

        else:
            ab = "  " + guesses[lastWord-1][letterPosition].upper()
            color_print(ab, color='green', end='')
else:
    for letterPosition in range(5): # prints 1 word
        if letterPosition == 0 : 

            color_print("| ", end='')
            color_print(guesses[lastWord-1][letterPosition].upper(), color='red', end='')

        elif letterPosition == 4:
            aa = "  " + guesses[-1][letterPosition].upper()
            color_print(aa, color='red', end='')
            color_print(" |")

        else:
            ab = "  " + guesses[lastWord-1][letterPosition].upper()
            color_print(ab, color='red', end='')

for i in range(6-lastWord):
   for letterPosition in range(5): # prints 1 word

        if letterPosition == 0 : 

            color_print("| ", color='magenta', end='')
            color_print(guesses[i+lastWord][letterPosition].upper(), color='white', end='')

        elif letterPosition == 4:
            aa = "  " + guesses[i+lastWord][letterPosition].upper()
            color_print(aa, color='white', end='')
            color_print(" |", color='magenta',)

        else:
            ab = "  " + guesses[i+lastWord][letterPosition].upper()
            color_print(ab, color='white', end='')

color_print(" --------------- ", color='magenta')

print("\n\n\n", wordle)