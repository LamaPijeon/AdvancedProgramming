import random
import os
firstplace=random.randint(0,15)
secondplace=random.randint(0,15)
while firstplace == secondplace:
   secondplace=random.randint(0,16)

board = [0,0,0,0,
         0,0,0,0,
         0,0,0,0,
         0,0,0,0]

# first two tiles popping up
newnum=[2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
firstnewnumchoose=random.randint(0,9)
secondnewnumchoose=random.randint(0,9)

board.pop(firstplace)
board.insert(firstplace, newnum[firstnewnumchoose])
board.pop(secondplace)
board.insert(secondplace, newnum[secondnewnumchoose])

movecount=0
exit="\n"

print("--------- -------- -------- ---------")

row = 0
for i in board:
 print("| ",f'{i:04d}', " ", end='')
 row = row + 1
 if row == 4:
    print('| ', end='')
    print()
    print("--------- -------- -------- ---------")
    row = 0
while True:
    
    ogboard=board
    move=input("What is your move? use  w,a,s,d as arrow keys : ")
    print(exit)
    
    if move=="w":
        for i in range(4):
            for z in range(3):
                if z == 0 or z==2: # remove zeros
                    for r in range(4): #repeats 4 times bc its dum
                        if board[8+i] == 0:
                            board[8+i] = board[12+i]
                            board[12+i] = 0
                        if board[4+i] == 0:
                            board[4+i] = board[8+i]
                            board[8+i] = 0
                        if board[i] == 0:
                            board[i] = board[4+i]
                            board[4+i] = 0
                if z==1: # this is where your adding thing goes.
                    if board[i]==board[4+i]:
                        board[i]+=board[4+i]
                        board[4+i]=0
                    elif board[4+i]==board[8+i]:
                        board[4+i]+=board[8+i]
                        board[8+i]=0
                    elif board[8+i]==board[12+i]:
                        board[8+i]+=board[12+i]
                        board[12+i]=0
    elif move=="a":
        for i in range(0, 16, 4):
            for z in range(3):
                if z == 0 or z==2: # remove zeros
                    for r in range(4): #repeats 4 times bc its dum
                        if board[2+i] == 0:
                            board[2+i] = board[3+i]
                            board[3+i] = 0
                        if board[1+i] == 0:
                            board[1+i] = board[2+i]
                            board[2+i] = 0
                        if board[i] == 0:
                            board[i] = board[1+i]
                            board[1+i] = 0
                if z==1: # this is where your adding thing goes.
                    if board[i]==board[1+i]:
                        board[i]+=board[1+i]
                        board[1+i]=0
                    elif board[1+i]==board[2+i]:
                        board[1+i]+=board[2+i]
                        board[2+i]=0
                    elif board[2+i]==board[3+i]:
                        board[2+i]+=board[3+i]
                        board[3+i]=0   
    elif move=="d":
        for i in range(0, 16, 4):
            for z in range(3):
                if z == 0 or z==2: # remove zeros
                    for r in range(4): #repeats 4 times bc its dum
                        if board[1+i] == 0:
                            board[1+i] = board[i]
                            board[i] = 0
                        if board[2+i] == 0:
                            board[2+i] = board[1+i]
                            board[1+i] = 0
                        if board[3+i] == 0:
                            board[3+i] = board[2+i]
                            board[2+i] = 0
                if z==1: # this is where your adding thing goes.
                    if board[3+i]==board[2+i]:
                        board[3+i]+=board[2+i]
                        board[2+i]=0
                    elif board[2+i]==board[1+i]:
                        board[2+i]+=board[1+i]
                        board[1+i]=0
                    elif board[1+i]==board[i]:
                        board[1+i]+=board[i]
                        board[i]=0    
    elif move=="s":
        for i in range(4):
            for z in range(3):
                if z == 0 or z==2: # remove zeros
                    for r in range(4): #repeats 4 times bc its dum
                        if board[4+i] == 0:
                            board[4+i] = board[i]
                            board[i] = 0
                        if board[8+i] == 0:
                            board[8+i] = board[4+i]
                            board[4+i] = 0
                        if board[12+i] == 0:
                            board[12+i] = board[8+i]
                            board[8+i] = 0
                if z==1: # this is where your adding thing goes.
                    if board[12+i]==board[8+i]:
                        board[12+i]+=board[8+i]
                        board[8+i]=0
                    elif board[8+i]==board[4+i]:
                        board[8+i]+=board[4+i]
                        board[4+i]=0
                    elif board[4+i]==board[i]:
                        board[4+i]+=board[i]
                        board[i]=0
    #no dum moves
    if ogboard==board:
        movecount+=1
        print(ogboard)
        print(board)
        print("dum")
    
    # os.system("clear")

    print("--------- -------- -------- ---------")

    row = 0
    for i in board:
        print("| ",f'{i:04d}', " ", end='')
        row = row + 1
        if row == 4:
            print('| ', end='')
            print()
            print("--------- -------- -------- ---------")
            row = 0
    print("your move count is", movecount, exit)