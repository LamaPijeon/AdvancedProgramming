# import random

# #1 Squares of 20

# for counter in range(1,21):
#     print(counter," squared is: ",counter**2)

# #2 9 green bottles challenge

# bottlesOnWall = int(input("How maby bottles of milk on the wall?  "))

# for counter in range(bottlesOnWall,0,-1):
#     print(counter, " bottles of milk on the wall, ",counter," bottles of milk. You take one down, you pass it around, ",counter-1," bottles of milk on the wall.")

# #3 Times table challenge 1

# timesTableNumber = int(input("what number for time table?   "))

# for counter in range(0,13):
#     print(counter," * ",timesTableNumber," = ",counter*timesTableNumber)












# #4 Fibonacci sequence challenge

# def reacouringFibinacci(x):
#    if x <= 1:
#        return x
#    else:
#        return(reacouringFibinacci(x-1) + reacouringFibinacci(x-2))

# print("Fibonacci sequence:")
# for counter in range(20):
#     print(reacouringFibinacci(counter))



# #5 Average calculator challenge

# numbersToAverage = int(input("How many numbers to be averaged?  "))
# average = 0

# for counter in range(0,numbersToAverage):
#     numbersAverage = int(input("Type in the numbers   "))
#     print(numbersAverage)
#     average = average + numbersAverage
#     print(average)

# print("The average of these ", numbersToAverage, " numbers is ", average/numbersToAverage)

# #6 FizzBuzz

# fizzBuzz = 1
# fizz = None
# buzz = None
# for counter in range(0,100):
#     if fizzBuzz % 5 == 0 and fizzBuzz % 3 == 0:
#         print("FizzBuzz")
#     elif fizzBuzz % 3 == 0 and fizzBuzz % 5 != 0:
#         print("Fizz")
#     elif fizzBuzz % 5 == 0 and fizzBuzz % 3 != 0:
#         print("Buzz")
#     else:
#         print(fizzBuzz)
#     fizzBuzz = fizzBuzz+1

# #7 Times table challenge 2

# correctAnswers = 0

# questiosnToAsk = int(input("How many questions would you like to be asked?  "))

# for counter in range(0,questiosnToAsk):
#     randomNum1 = random.randint(0,9)
#     randomNum2 = random.randint(1,9)

#     if randomNum2 > randomNum1:
#         specialNumber = randomNum1
#         randomNum1 = randomNum2
#         randomNum2 = specialNumber

#     operation = random.randint(1,4)

#     if operation == 1:
#         equation = "What is the answer to:  ", str(randomNum1), "+", str(randomNum2)
#         tableAnswer = int(input(equation))
#         if tableAnswer == randomNum1 + randomNum2:
#             print("YOUR ANSWER IS CORRECT")
#             correctAnswers = correctAnswers + 1
#         else:
#             print("YOUR ANSWER IS WRONG")
#     elif operation == 2:
#         equation = "What is the answer to:  ",str(randomNum1),"-",str(randomNum2)
#         tableAnswer = int(input(equation))
#         if tableAnswer == randomNum1 - randomNum2:
#             print("YOUR ANSWER IS CORRECT")
#             correctAnswers = correctAnswers + 1
#         else:
#             print("YOUR ANSWER IS WRONG")
#     elif operation == 3:
#         equation = "What is the answer to:  ",str(randomNum1),"//",str(randomNum2)
#         tableAnswer = int(input(equation))
#         if tableAnswer == randomNum1 // randomNum2:
#             print("YOUR ANSWER IS CORRECT")
#             correctAnswers = correctAnswers + 1
#         else:
#             print("YOUR ANSWER IS WRONG")
#     elif operation == 4:
#         equation = "What is the answer to:  ",str(randomNum1),"*",str(randomNum2)
#         tableAnswer = int(input(equation))
#         if tableAnswer == randomNum1 * randomNum2:
#             print("YOUR ANSWER IS CORRECT")
#             correctAnswers = correctAnswers + 1
#         else:
#             print("YOUR ANSWER IS WRONG")
    
# print("You got ",correctAnswers," answers correct out of ",questiosnToAsk," questions. Congrats")

#8 ROT13


cipher = input("Do you want to cypher or decypher (c or d)  ")
cipheredText = ""
if cipher == "c":
    toCipher = input("Input the text to be cyphered   ")
    cipherLen = len(toCipher)
    for count in range(0,cipherLen):
        cipherLetter = toCipher[count]
        i = ord(cipherLetter)+13
        if i > 256:
            i = i - 256
        cipheredLetter = chr(i)
        cipheredText = cipheredText+cipheredLetter
    print(cipheredText)

elif cipher == "d":
    toCipher = input("Input the text to be decyphered   ")
    cipherLen = len(toCipher)

    for count in range(0,cipherLen):
        cipherLetter = toCipher[count]
        i = ord(cipherLetter)-13
        if i < 0:
            i = 256-abs(i)
        decipheredLetter = chr(i)
        cipheredText = cipheredText+decipheredLetter
    print(cipheredText)

#9 Letter game challenge

specialWord = input("What is the word that you'd like to check the point of?  ").lower()
specialWordLen = len(specialWord)
wordsPoints = 0

for count in range(0,specialWordLen):
    specialLetter = specialWord[count]
    if specialLetter == "a":
        wordsPoints += 2       
    elif specialLetter == "b":
        wordsPoints += 17
    elif specialLetter == "c":
        wordsPoints += 10
    elif specialLetter == "d":
        wordsPoints += 12
    elif specialLetter == "e":
        wordsPoints += 1
    elif specialLetter == "f":
        wordsPoints += 18
    elif specialLetter == "g":
        wordsPoints += 16
    elif specialLetter == "h":
        wordsPoints += 15
    elif specialLetter == "i":
        wordsPoints += 4
    elif specialLetter == "j":
        wordsPoints += 25
    elif specialLetter == "k":
        wordsPoints += 21
    elif specialLetter == "l":
        wordsPoints += 9
    elif specialLetter == "m":
        wordsPoints += 14
    elif specialLetter == "n":
        wordsPoints += 7
    elif specialLetter == "o":
        wordsPoints += 5
    elif specialLetter == "p":
        wordsPoints += 13
    elif specialLetter == "q":
        wordsPoints += 26
    elif specialLetter == "r":
        wordsPoints += 3
    elif specialLetter == "s":
        wordsPoints += 8
    elif specialLetter == "t":
        wordsPoints += 6
    elif specialLetter == "u":
        wordsPoints += 11
    elif specialLetter == "v":
        wordsPoints += 22
    elif specialLetter == "w":
        wordsPoints += 20
    elif specialLetter == "x":
        wordsPoints += 23
    elif specialLetter == "y":
        wordsPoints += 19
    elif specialLetter == "z":
        wordsPoints += 24
print("this word is ",wordsPoints," points")