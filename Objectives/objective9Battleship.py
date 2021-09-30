import random
import os
from getpass import getpass
import time

def attackSpace(space, playerBoard, playerHit):
    removeHit(playerHit, space)
    space = str(space)
    letter = str(space[0]).upper()
    number = str(space)[1]
    space = letter+number
    playerBoardNums = playerBoard[1]
    playboardLetts = playerBoard[0]
    for x in range(0,len(playerBoard[0])):
        if playboardLetts[x] == letter:
            if str(playerBoardNums[x]) == str(number):
                ifHit(playerBoard, x, space)
                break

def removeHit(playhit, space):
    space = str(space)
    letter = str(space[0]).lower()
    number = str(space)[1]
    letterLocation = ord(letter)-96

    playhit[int(number)].pop(int(letterLocation))
    playhit[int(number)].insert(int(letterLocation),"x")

    for x in range(0,6):
        if x == 0:
            print("",playhit[0][x],playhit[1][x],playhit[2][x],playhit[3][x],playhit[4][x],playhit[5][x])
        else:
            print(playhit[0][x],playhit[1][x],playhit[2][x],playhit[3][x],playhit[4][x],playhit[5][x])

def ifHit(board, location, space):
    print("Congrats. ",space," was a hit")
    board[0].pop(location)
    board[0].insert(location,"*")
    board[1].pop(location)
    board[1].insert(location, "*")

player1Board = [["","","","",""],["","","","",""]]
player2Board = [["","","","",""],["","","","",""]]
count = 0
print("You get four 1x1 ships in this 5,5 field. Choose location. First type number 1-5, then type letter A-E. Repeat this process 3 more times.")
print()

# adds first players ships to the map

for x in range(0,5):
    count += 1
    print("what's the letter of the ",count," place? Press enter after entered.")
    letter = input("A-E:   ").upper()
    print("what's the number of the ",count," place? Press enter after entered.")
    number = input("1-5:   ").lower()
    player1Board[0].insert(count-1,letter)
    player1Board[1].insert(count-1,number)
    print()

# prints first players board, then deletes it so other player doesn't see
for x in range(0,5):
    print(player1Board[0][x],player1Board[1][x])
print("Player 1. These are your pieces.")
time.sleep(4)
os.system('clear')

# adds seconds players ships to the map

count = 0
for x in range(0,5):
    count += 1
    print("what's the letter of the ",count," place? Press enter after entered.")
    letter = input("A-E:   ").upper()
    print("what's the number of the ",count," place? Press enter after entered.")
    number = input("1-5:   ").lower()
    player2Board[0].insert(count-1,letter)
    player2Board[1].insert(count-1,number)
    print()

# prints second players board, then deletes it so other player doesn't see

for x in range(0,5):
    print(player2Board[0][x],player2Board[1][x])
print("Player 2. These are your pieces.")
time.sleep(4)
os.system('clear')

player1Hits = [["","A","B","C","D","E"],["1","o","o","o","o","o"],["2","o","o","o","o","o"],["3","o","o","o","o","o"],["4","o","o","o","o","o"],["5","o","o","o","o","o"]]
player2Hits = [["","A","B","C","D","E"],["1","o","o","o","o","o"],["2","o","o","o","o","o"],["3","o","o","o","o","o"],["4","o","o","o","o","o"],["5","o","o","o","o","o"]]
turn = 1

while ("1" in player1Board[1] or "2" in player1Board[1] or "3" in player1Board[1] or "4" in player1Board[1] or "5" in player1Board[1]) and ("1" in player2Board[1] or "2" in player2Board[1] or "3" in player2Board[1] or "4" in player2Board[1] or "5" in player2Board[1]):
    
    if turn == 1: 
        locationHit = input("Where is the location to hit (i.e: A3) :  ")
        attackSpace(locationHit, player2Board, player1Hits)
        turn += 1
    else:
        locationHit = input("Where is the location to hit (i.e: A3) :  ")
        attackSpace(locationHit, player1Board, player2Hits)
        turn -=1
    print()
    print()

if len(player1Board[1]) !=0:
    print("PLAYER 1 WINS")
else:
    print("PLAYER 2 WINS")