import random
import math
import time

#1 Menu selection challenge

gamenumber = 0
while gamenumber != 1 or gamenumber != 2 or gamenumber != 3:
    print()
    gamenumber = (input("1 = Play Game, 2 = Instructions, 3 = Quit. What do you want to do? (input number):   "))
    print()

    if gamenumber == "1":
        gamenumber = 1
    elif gamenumber == "2":
        gamenumber = 2
    elif gamenumber == "3":
        gamenumber = 3

    if gamenumber == 1:
        print("Lets Play")
        break
    elif gamenumber == 2:
        print("Get brain cells not instructions")
        break
    elif gamenumber == 3:
        print("Cya")
        break
        print()

#2 Compound interest challenge
    
startingBalance = float(input("How much money do you have now?   "))
print()
endBalance = float(input("How much money do you want to have?   "))
print()
years = 0
while startingBalance < endBalance:
    startingBalance = startingBalance*1.4
    years += 1
    print("In ", years, "years, youll have $", round(startingBalance, 2))
    print()

#3 Guess the number game challenge challenge
    
randomNum = random.randint(0,100)
guesses = 0
guess = 1000

while guess != randomNum:
    guess = int(input("What number do you think it is?"))
    print()
    if guess > randomNum:
        print("You're number is too high")
        print()
    elif guess < randomNum:
        print("You're number is too low")
        print()
    else:
        print("DING DING DING. YOU WIN. IT ONLY TOOK ", guesses, "TRIES")
        print()
    guesses += 1

#4 Gamertag challenge

gamerTag = None
valid_gamertag = False

while valid_gamertag == False:
    print()
    gamerTag = input("What would you like you gamer tag to be?   ")
    print()
    if 15 > len(gamerTag):
        print("Gamer tag is acceptable. Your gamer tag is now ", gamerTag)
        valid_gamertag = True
    else: 
        print("Your gamer tag is too long. Must be less then 15 character. Make it shorter. ", len(gamerTag)-15 ," characters shorter to be exact.")

#5 Rock, paper, scissors challenge

computerPoits = 0
playPoints = 0
win = False

while win == False:
    computerMove = random.choice(('rock', 'paper', 'scissors'))
    playerMove = input("Rock, Paper or scissors? ").lower()
    print()
    print(playerMove)
    print(computerMove)
    print()
    if playerMove == "rock":
        if computerMove == "rock":
            print("Tie. Computer did rock too.")
        elif computerMove == "paper":
            computerPoits += 1
            print("Computer did paper. +1 points for them")
        else:
            playPoints += 1
            print("Computer did scissors. +1 points for you") 

    elif playerMove == "paper":

        if computerMove == "paper":
            print("Tie. Computer did paper too.")
        elif computerMove == "scissors":
            computerPoits += 1
            print("Computer did scissors. +1 points for them")
        else:
            playPoints += 1
            print("Computer did rock. +1 points for you")    

    elif playerMove == "scissors":

        if computerMove == "scissors":
            print("Tie. Computer scissors rock too.")
        elif computerMove == "rock":
            computerPoits += 1
            print("Computer did rock. +1 points for them")
        else:
            playPoints += 1
            print("Computer did paper. +1 points for you")    

    else:
        print("You wrote something that wasn't valid. -1 Points for you")
       
        if playPoints > 0:
            playPoints -= 1
    if computerPoits == 10 or playPoints == 10:
        win = True
    print("Computer Points:  ", computerPoits)
    print("Player Points:   ", playPoints)
    print()

print("winner winner, chicken dinner")

if computerPoits == 10:
    print("Sorry, but you lose. You weren't worthy. ",computerPoits-playPoints, "points behind the computer with ",playPoints,". Better luck next time.")
else:
        print("You did it. You're worthy. Computer was ",playPoints-computerPoits, "points behind you with ",computerPoits,".")

#6 Happy numbers challenge

specialNumber = abs(int(input("what's the number   ")))
ogNumber = specialNumber
numlist = [specialNumber]
valid = True
solved = False 
workProgress = 0    

while valid == True and solved != True:
    specialWordLen = len(str(specialNumber))
    for count in range(0,specialWordLen):
        intsInSpecial = str(specialNumber)[count]
        workProgress = int(workProgress) + int(intsInSpecial)**2
    specialNumber = workProgress
    print(specialNumber) 
    workProgress = 0
    if specialNumber in numlist:
        print("it's in the list")
        valid = False
    if specialNumber == 1:
        solved = True
    numlist.append(specialNumber)

#7 XP Challenge

xp = 0
leftoverXp = 0
playerRank = 1

while xp <= 2000:
    xpEarned = int(input("How much xp did you earn:   "))
    xp += xpEarned
    if playerRank == 1:
        if xp >= 100:
            leftoverXp = xp-100
            xp = leftoverXp
            playerRank += 1
            print("You have been promoted")
    elif playerRank == 2:
        if xp >= 300:
            leftoverXp = xp-300
            xp = leftoverXp
            playerRank += 1
            print("You have been promoted")
    elif playerRank == 3:
        if xp >= 700:
            leftoverXp = xp-700
            xp = leftoverXp
            playerRank += 1
            print("You have been promoted")
    elif playerRank == 4:
        if xp >= 1500:
            leftoverXp = xp-1500
            xp = leftoverXp
            playerRank += 1
            print("You have been promoted")
    print(xp,"xp")
    print("Rank: ",playerRank)
    print()