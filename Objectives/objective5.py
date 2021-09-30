import random

#1 Dice Problem
sidesOnDice = int(input("How many sides on dice?"))
DiceResult = random.randint(1,sidesOnDice)
print(DiceResult)

#2 Divisable Challenge
num1 = int(input("First number   "))
num2 = int(input("second number   "))

if num1 % num2 == 0:
    print("They are perfectly divisable by eachother")
else:
    print("they're not divisable and the remainder is ",num1%num2)

#3 Month Challenge
monthNum = int(input("What is the month number   "))

if monthNum == 1:
    print("January 31 days")
elif monthNum == 2:
    leapYear = int(input("What year is it  "))
    if leapYear % 4 == 0:
        print("February 29 days")
    else:
        print("February 28 days")
elif monthNum == 3:
    print("March 31 days")
elif monthNum == 4:
    print("April 30 days")
elif monthNum == 5:
    print("May 31 days")
elif monthNum == 6:
    print("June 30 days")
elif monthNum == 7:
    print("July 31 days")
elif monthNum == 8:
    print("August 31 days")
elif monthNum == 9:
    print("September 30 days")
elif monthNum == 10:
    print("October 31 days")
elif monthNum == 11:
    print("November 30 days")
elif monthNum == 12:
    print("December 31 days")
else:
    print("Sorry. must be between 1-12")

#4 Moth Challenge

blank = input("Type 'ROLL DICE' to roll the first dice  ")
dice1 = random.randint(1,6)
print(dice1)
blank = input("Type 'ROLL DICE' to roll the second dice  ")
dice2 = random.randint(1,6)
print(dice2)
blank = input("Type 'ROLL DICE' to roll the third dice  ")
dice3 = random.randint(1,6)
print(dice3)

if dice3 == dice2 == dice1:
    diceScore = dice3*3
elif dice3 == dice1:
    diceScore = dice3+dice1
elif dice2 == dice1:
    diceScore = dice2+dice1
elif dice3 == dice2:
    diceScore = dice3+dice2
else:
    diceScore = 0

print("Your score is:  ", diceScore)