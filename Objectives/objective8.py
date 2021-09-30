import random

# #1 Vat Challenxe

# def vatCalulate(money):
#     vat = money*1.23
#     return vat


# price = float(input("What's the price :  "))
# print(vatCalulate(price))

#2 Conversion challenge

def inch2Cm(measurement):
    output = measurement*2.54
    return output

def cm2Inch(measurement):
    output = measurement/2.54
    return output

def kg2Pound(measurement):
    output = measurement*2.205
    return output

def pound2Kg(measurement):
    output = measurement/2.205
    return output

mFrom = input("Mass or length (m or l)? :  ").lower()

if mFrom == "m":
    mFrom = input("From kg or lb? :  ").lower()
    amount = float(input("How much? :  "))
    if mFrom == "kg":
        print(amount, "kg is equal to ",kg2Pound(amount)," pounds")
    elif mFrom == "lb":
        print(amount, "pounds is equal to ",pound2Kg(amount)," kg")

elif mFrom == "l":
    mFrom = input("From inches or cm? :  ").lower()
    amount = float(input("How much? :  "))
    if mFrom == "inches":
        print(amount, "inches is equal to ",inch2Cm(amount)," cm")
    elif mFrom == "cm":
        print(amount, "cm is equal to ",cm2Inch(amount)," inches")

# 3 Conversion challenge part 2

print()
print("Iches, cm, kg, lb")
print()
amountThings = input("Input amount and unit (e.g. 25 cm to inches) :  ")
print()

spaceLocation1 = amountThings.find(" ")
amount = amountThings[:spaceLocation1]

spaceLocation2 = spaceLocation1 + amountThings[spaceLocation1:].find(" ")
lastSpace = amountThings.rfind(" ")

mFrom = amountThings[spaceLocation1+1:spaceLocation1+spaceLocation2+1]

mTo = amountThings[lastSpace+1:]
print(amount)
print(mFrom)
print(mTo)

if mFrom == "kg":
    print(amount, "kg is equal to ",kg2Pound(amount)," pounds")
elif mFrom == "lb":
    print(amount, "pounds is equal to ",pound2Kg(amount)," kg")

if mFrom == "inches":
    print(amount, "inches is equal to ",inch2Cm(amount)," cm")
elif mFrom == "cm":
    print(amount, "cm is equal to ",cm2Inch(amount)," inches")

#4/5 Darts challenge
toRestart = None
playerScore1 = 501
playerScore2 = 501
turn = 1

print("New game. Players starts at 501 points.")

def removePoints(points, playerScore, turn):
    if turn == 1:
        if playerScore - points >= 1:
            playerScore -= points
            print(playerScore)
        if playerScore - points == 0:
            playerScore = 0
            print("Player 1 wins")
            toRestart = input("Do you want to restart the game (y or n)? :  ")
            if toRestart == "y":
                playerScore1 = 501
                playerScore2 = 501
        return playerScore
    if turn ==2:
        if playerScore - points >= 1:
            playerScore -= points
            print(playerScore)
        if playerScore - points == 0:
            playerScore = 0
            print("Player 2 wins")       
        return playerScore

while playerScore1 != 0 and playerScore2 != 0:
    if turn == 1:
        print("Player 1")
        dartPoints = int(input("What was the score from your three shots :  "))
        playerScore1 = removePoints(dartPoints, playerScore1, turn)
        if playerScore1 == 0:
            toRestart = input("Do you want to restart the game (y or n)? :  ")
            if toRestart == "y":
                playerScore1 = 501
                playerScore2 = 501   
                turn = 1  
        print()
        turn = 2
    else:
        print("Player 2")
        dartPoints = int(input("What was the score from your three shots :  "))
        playerScore2 = removePoints(dartPoints, playerScore2, turn)
        print()
        turn = 1
        if playerScore1 == 0:
            toRestart = input("Do you want to restart the game (y or n)? :  ")
            if toRestart == "y":
                playerScore1 = 501
                playerScore2 = 501   
                turn = 1  

# 6/11 Snake eyes challenge

player1Score = 0
player2Score = 0
runningTotal = 0
turn = 0

def start(bank):
    runningScore = 0
    live = 1
    bank = bank

    while live == 1:
        print()
        live, bank = calculateDice(runningScore, live, bank)
        # live, bank = newList[0], newList[1]
        print()
    return bank

def calculateDice(runScore, live, bank):
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    totalDice = 0
    runScore = runScore

    print("Dice 1 :  ", d1)
    print("Dice 2 :  ", d2)
    totalDice = d1+d2

    if d1 != 1 and d2 != 1:
        runScore += totalDice
        print("Running total :  ", runScore,"       Bank total :  ",bank)
        gamble = input("Would you like to gamble? (y or n) :  ")
        live = 1
        if gamble == "y":
            print()
            live, bank = calculateDice(runScore, live, bank)
            return live, bank
            print()
            print()
        else:
            bank += runScore
            live = 2
            # newList = [live, bank]
            return live, bank
        
    elif d1 == 1 and d2 == 1:
        print("Sorry. You roled skunk eyes. Bye bye money!")
        live = 2
        bank = 0
        
        # newList = [int(live), int(bank)]
        return live, bank

    elif d1 == 1 or d2 == 1:
        print("Sorry. You rolled a one. Sure, your running score will be taken away but at least youll still have money in the bank?")
        live = 2
        if bank != 0:
            bank = bank
        else:
            bank = 0
        # newList = [live, bank]
        return live, bank


while player1Score < 100 and player2Score < 100:
    if turn == 0:
        player1Score = int(start(player1Score))
        print("Player1 score is :  ", player1Score)
        print()
        print()
        turn += 1
    else:
        player2Score = start(player2Score)
        print("Player2 score is :  ", player2Score)
        print()
        print()
        turn -= 1
if player2Score < player1Score:
    print("Congrats Player1. You win with ", player1Score," points. This is ",player1Score-player2Score," points infront of your opponent.")
else:
    print("Congrats Player2. You win with ", player2Score," points. This is ",player2Score-player1Score," points infront of your opponent.")

# 9/10 Pass the Pigs challenge

pig1Score = 0
pig2Score = 0
turn = 0
pig1Turns = 0
pig2Turns = 0

def pigScore(pigBank):
    input("")
    print()
    pigA = random.randint(1,6)
    pigB = random.randint(1,6)
    #1 = side, 2 = other, 3 = feet
    if pigA == pigB == 1:
        pigBank += 1
        print("Sider. +1 Point")
    elif pigA == pigB == 2:
        pigBank += 1
        print("Sider. +1 Point")
    elif pigA == pigB == 3:
        pigBank += 20
        print("double trotter. +20 Points")
    elif pigA == 3 or pigB == 3:
        pigBank += 5
        print("trotter. +5 points")
    elif pigA == 1 or pigB == 2:
        pigBank = 0
        print("death. Lose Bank")
    elif pigA == 2 or pigB == 1:
        pigBank = 0
        print("death. Lose bank")
    elif pigA == 4 or pigB == 4:
        pigBank += 5
        print("Snouter")
    elif pigA == 4 and pigB == 4:
        pigBank += 20
        print("double Snouter")
    elif pigA == 5 or pigB == 5:
        pigBank += 5
        print("Razorback")
    elif pigA == 5 and pigB == 5:
        pigBank += 20
        print("double Razorback")
    pigBank
    print()
    return pigBank

while pig1Score < 100 and pig2Score < 100:
    if turn == 0:
        print("Player1 :  ")
        pig1Score = pigScore(pig1Score)
        print("Score :  ", pig1Score)
        turn += 1
        pig1Turns += 1
        print(pig1Turns," turns")
    else:
        print("Player2 :  ")
        pig2Score = pigScore(pig2Score)
        print("Score :  ",pig2Score)
        turn -= 1
        pig2Turns +=1
        print(pig2Turns," turns")
    print()
if pig1Score > pig2Score:
    print("congrats player 1. You win")
elif pig1Score < pig2Score:
    print("congrats player 2. You win")