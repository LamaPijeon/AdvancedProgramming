# IMPORTS
import os
import time as ti
from lazyme.string import color_print
import csv
import random
import random

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

        i = 0                                  # 'misplaced': [['a','b','c'],[],[],[],[]]
        for y in letters['misplaced']:         # y = ['a','b','c']
            if deleted == False and y != []: 
                for z in y:                    # z = 'a'
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
    randomNumber = random.randint(0, len(possibleWords))
    wordlelele = possibleWords[randomNumber]
    duplicates = False

    for x in range(5):
        for y in range(5):
            if wordlelele[x] in wordlelele[y]: inWord += 1
        if inWord > 1: 
            duplicates = True
            possibleWords.pop(randomNumber)
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
                if guess[i] in letters['misplaced'][x]: 
                    letters['misplaced'][x].remove(guess[i])
        elif guess[i] in wordle and guess[i] not in letters['misplaced'][i] and guess[i] not in letters['correct']: 
            letters['misplaced'][i].append(guess[i])
            wordsForSure.append(guess[i])
        elif guess[i] not in wordle and guess[i] not in letters['wrong']: 
            letters['wrong'].append(guess[i])

    if guess == wordle: return 6, True
    else: return t, False

def takeGuess(tries):
    guessCorrect = False
    while guessCorrect == False:
        print(nextGuess)
        newGuess = input("What's your next guess:  ").lower()
        if len(newGuess) == 5 and newGuess in allowedWords.values(): guessCorrect = True
        if newGuess == "p": 
            print(possibleWords)

    guesses[tries] = list(newGuess)

    return newGuess

def programGuessRemoval(testGuess, testWordle):
    wrong = letters['wrong'][:]
    correct = letters['correct'][:]
    misplaced = []
    for i in range(5):
        misplaced.append(letters['misplaced'][i][:])

    for i in range(5):
        guessLetter = testGuess[i]
        letterDone = True

        if guessLetter == testWordle[i]: # if the letter is green
            letterDone = False
            correct[i] = guessLetter # checked
            for x in range(5):
                if guessLetter in misplaced[x]:
                    misplaced[x].remove(guessLetter)

        elif guessLetter in testWordle and letterDone == True : 
            letterDone = False
            misplaced[i].append(guessLetter)

        elif guessLetter not in testWordle and guessLetter not in wrong and letterDone == True : # if the letter is gray
            wrong.append(guessLetter) #checked

    return {'wrong':     wrong,
            'correct':   correct,
            'misplaced': misplaced}

def whatsTheWinner(options):

    '''
    
    options is the array of options it would eliminate

    inputs       answers
           frogs  doors shtik
    shtik  [[53,   23,   12],
    frogs   [34,   53,   21]
    doors   [12,   23,   53]]
    
    '''

    averageRow = [int((sum(x)/len(x))) for x in options] # x = row with 1 input
    totalRow = [max(x) for x in options] # x = row with 1 input

    finalRow = [a + b for a, b in zip(averageRow, totalRow)]

    maxFinalRow = max(finalRow)

    if finalRow.count(maxFinalRow) == 1:
        return finalRow.index(maxFinalRow)

    indexes = [] # this will become position of all max values

    for i in range(finalRow.count(maxFinalRow)):
        indexes.append(finalRow.index(maxFinalRow))
        finalRow.pop(finalRow.index(maxFinalRow))


    for i in range(len(options)):
        print(allowedWords[i], possibleWords[i], options[i])
        ti.sleep(.01)

    if len(finalRow) <= 15:
        bestGuessValue = 'monkay'
        bestGuessPosition = 'monkay'
        for i in range(len(indexes)):
            if allowedWords[indexes[i]] in possibleWords.values():
                bestGuessValue = totalRow[indexes[i]]
                bestGuessPosition = indexes[i]
            if bestGuessPosition != 'monkay':
                if totalRow[indexes[i]] > bestGuessValue and allowedWords[indexes[i]] in possibleWords.values():
                    bestGuessValue = totalRow[indexes[i]]
                    bestGuessPosition = indexes[i]
        
        if bestGuessPosition != 'monkay' : return bestGuessPosition

    if t == 6:
        bestGuessValue = averageRow[indexes[0]]
        bestGuessPosition = indexes[0]

        for i in range(len(indexes)):
            if averageRow[indexes[i]] > bestGuessValue and allowedWords[indexes[i]] in possibleWords.values():
                bestGuessValue = averageRow[indexes[i]]
                bestGuessPosition = indexes[i]

        return bestGuessPosition
        
    bestGuessValue = averageRow[indexes[0]]
    bestGuessPosition = indexes[0]

    for i in range(len(indexes)):
        if averageRow[indexes[i]] > bestGuessValue:
            bestGuessValue = averageRow[indexes[i]]
            bestGuessPosition = indexes[i]

    return bestGuessPosition

    # averageRowOld = [int((sum(x)/len(x))) for x in options] # x = row with 1 input
    # averageRow = {}

    # for i in range(len(averageRowOld)):
    #     averageRow[i] = averageRowOld[i]

    # if len(options) >= 10: # if it's more than 10, we remove the 10% of words that are worst for sure
    #     deleteNum = round(len(options)/10)

    #     for i in range(deleteNum):
    #         minValue = averageRow[list(averageRow.keys())[0]]
    #         minPlace = 0
    #         for x in averageRow:
    #             if averageRow[x] < minValue: 
    #                 minValue = averageRow[x]
    #                 minPlace = x
    #         averageRow.pop(minPlace)
    #         print(minValue, minPlace)
    #         ti.sleep(2)
        # return

def wordFinder():
    options = []
    position = 0

    for guess in allowedWords.values():
        options.append([])
        for answer in possibleWords.values(): 
            wordsRemoved = 0

            testLetters = programGuessRemoval(guess, answer)

# --------------------------------------------------------------------------------------------------------

            newPossiblewords = possibleWords.copy()

            for wordNum in range(len(possibleWords)):

                deleted = False

                for letter in testLetters['wrong']:
                    if deleted == False and letter in newPossiblewords[wordNum]: 
                        deleted = True
                        newPossiblewords.pop(wordNum)

                i = 0

                for correct in testLetters['correct']:
                    if deleted == False:
                        if correct != newPossiblewords[wordNum][i] and correct != '': 
                            deleted = True
                            newPossiblewords.pop(wordNum)
                    i += 1

                i = 0                                  # 'misplaced': [['a','b','c'],[],[],[],[]]
                for y in testLetters['misplaced']:         # y = ['a','b','c']
                    if deleted == False and y != []: 
                        for z in y:                    # z = 'a'
                            if deleted == False: 
                                if z not in newPossiblewords[wordNum]:
                                    deleted = True
                                    newPossiblewords.pop(wordNum)
                                elif z == newPossiblewords[wordNum][i]:
                                    deleted = True
                                    newPossiblewords.pop(wordNum)
                    i += 1

            testPossibleWords = [x for x in newPossiblewords.values()]

# --------------------------------------------------------------------------------------------------------

            wordsRemoved = len(possibleWords) - len(testPossibleWords)
            options[position].append(wordsRemoved)

        position += 1
    soWhatTheWinner = whatsTheWinner(options)
    print(soWhatTheWinner)
    print(allowedWords[soWhatTheWinner])
    ti.sleep(2)

    return allowedWords[whatsTheWinner(options)]

winner = False
possibleWords = {}
allowedWords = {}
wordsForSure = []
t = 0

letters = {'wrong': [],
           'correct': ['','','','',''],
           'misplaced': [[],[],[],[],[]]}     

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

nextGuess = ("pineapple teeheehee")

print(wordle)
ti.sleep(.2)

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
    nextGuess = wordFinder()
    t += 1

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