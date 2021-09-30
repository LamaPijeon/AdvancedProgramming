import random

# 1 Text dice challenge

dice = ["one", "two", "three", "four", "five", "six"]
print(dice[random.randint(0, 5)])

# 2 Notebook challenge

repeatNote = True
notes = ["","","","","","","","","",""]
while repeatNote == True:
    for count in range (0,9):
        print(count+1,": ",notes[count])
    print()
    noteChange = int(input("Which number note to change?: "))-1
    print()
    newnote = input("What's the new note: ")
    notes.pop(noteChange)
    notes.insert(noteChange, newnote)
    quit = input("Do you want to quit? (y or n): ")
    if quit == "y":
        break
    print()
    print()

# 3 Currency converter challenge

currencyArray = ["british", 0.19, "polish", 1, "american", 0.25, "vietnamese", 5834.44]

currencyStart = input("What currency you start with (i.e: British, Polish, American, Vietnamese):  ")
moneyAmount = float(input("How much money do you start with:  "))
currencyEnd = input("What currency you end with (i.e: British, Polish, American, Vietnamese):  ")

if currencyStart.lower() in currencyArray:
    startExchange = currencyArray.index(currencyStart)+1
    currencyMult = 1 / currencyArray[startExchange]
    endExchange = currencyArray.index(currencyEnd)+1
    amountEnd = moneyAmount*(currencyMult/currencyArray[endExchange])
    print(moneyAmount," ",currencyStart," to ", currencyEnd," is ",amountEnd," ", currencyEnd)

    print("starExchange ", currencyArray[startExchange])
    print(currencyMult," currencyMult")
    print("endExchange ", currencyArray[endExchange])
    print(amountEnd," amount end")

# 4 Battleships challenge

battleshipLocation = random.randint(1,5)
spacesHit = []
shipDestroyed = False
shipTurns = 0
alreadHit = False

while shipDestroyed == False:
    shipTurns += 1
    playhit = int(input("What square to hit (1-4): "))
    spacesHit.append(playhit)
    if playhit in spacesHit:
        print("you already hit there. Try again")
        alreadHit = True
    if playhit == battleshipLocation and alreadHit == False:
        print("Congrats. You hit it. Only ", shipTurns," turns needed")
        shipDestroyed = True
    
# 5 