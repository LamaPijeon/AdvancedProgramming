import os
from pynput import keyboard, mouse
import time

kBoard = keyboard.Controller()
moose = mouse.Controller()

class  snakeDo():
   
    def __init__(self):
        def leftMove(sideTime):
            kBoard.press('a')
            time.sleep(sideTime)
        def downMove(downTime):
            kBoard.press('s')
            time.sleep(downTime)
        def rightMove(sideTime):
            kBoard.press('d')
            time.sleep(sideTime)
        def upMove(downTime):
            kBoard.press('w')
            time.sleep(downTime)
        def reset(sideTime, upTime, resetTime, blockSpeed):
            leftMove(sideTime)
            downMove(upTime + .73*blockSpeed)           
            time.sleep(sideTime)
            rightMove(resetTime)
            upMove(upTime + .73*blockSpeed)           
        # boardSize = input("Board size Small, Medium, Large  (s, m, l) :  ")
        # speed = input("Board size slow, normal, fast  (s, n, f) :  ")
        
        boardSize = (9,10) 
        speed = 'f'

        # if boardSize == "s":
        #     boardSize = (9, 10)
        # elif boardSize == "m":
        #     boardSize = (15, 17)
        # elif boardSize == "l":
        #     boardSize = (21,24)
        time.sleep(1)
        moose.position = (1050, 675)
        moose.click(mouse.Button.left)
        time.sleep(1)
        moose.click(mouse.Button.left)
        kBoard.press('t')
        time.sleep(1)
        kBoard.press('d')
        if boardSize == (9, 10) and speed == 's':
            blockSpeed = 0.209
            time.sleep(1.2)
            kBoard.press('w')
            time.sleep(.7)
            death = False
            for x in range(10):
                upTime = 1.28
                sidetime = .15
                for i in range(4):
                    leftMove(sidetime)
                    downMove(upTime)
                    leftMove(sidetime)
                    upMove(upTime)
                reset(sidetime, upTime, 1.65, blockSpeed)
        elif boardSize == (9, 10) and speed == 'n':
            blockSpeed = .1576
            time.sleep(5.5*blockSpeed)
            kBoard.press('w')
            time.sleep(3.5*blockSpeed)
            death = False
            for x in range(10):
                upTime = blockSpeed * 6.2
                sidetime = blockSpeed * .6
                for i in range(4):
                    leftMove(sidetime)
                    downMove(upTime)
                    leftMove(sidetime)
                    upMove(upTime)
                reset(sidetime, upTime, blockSpeed * 7.5, blockSpeed)
        elif boardSize == (9, 10) and speed == 'f':
            blockSpeed = 0.104
            time.sleep(5.5*blockSpeed)
            kBoard.press('w')
            time.sleep(3.5*blockSpeed)
            death = False
            for x in range(10):
                upTime = blockSpeed * 6.169
                sidetime = blockSpeed * .6
                for i in range(4):
                    leftMove(sidetime)
                    downMove(upTime)
                    leftMove(sidetime)
                    upMove(upTime)
                reset(sidetime, upTime, blockSpeed * 7.2, blockSpeed)
        # elif boardSize == (15, 17) and speed == 's':
        # elif boardSize == (15, 17) and speed == 'n':
        # elif boardSize == (15, 17) and speed == 'f':
        # elif boardSize == (21,24) and speed == 's':
        # elif boardSize == (21,24) and speed == 'n':
        # elif boardSize == (21,24) and speed == 'f':
    # def up(upTime):
    # def down(upTime):
    # def right(sideTime):

snakeSolver = snakeDo()