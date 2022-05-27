import time as ti
import os
while True:
    hours = float(input("Hours : "))
    minutes = float(input("minutes : "))
    time = (minutes*60 + hours*3600)/3600
    print(time)
    ti.sleep(2)
    os.system("clear")