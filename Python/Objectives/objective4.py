#1

age = int(input("How old are you?:  "))

if age > 18:
    print("Over 18")
elif age < 18:
    print("Under 18")
else:
    print("You're 18")

#######################################################################

#2

waterTemp = int(input("What's the temperature of the water (in Centigrade)?:   "))

if waterTemp <= 0:
    print("Water is frozen")
elif waterTemp >= 100:
    print("Water is boiling")
else:
    print("Water is liquid")

#####################################################################

#3

testScore = int(input("What is the test score (out of 100)?:   "))

if testScore < 40:
    print("FAIL")
elif 60 > testScore >= 40:
    print("PASS")
elif 80 > testScore >= 60:
    print("MERIT")
else:
    print("DISTINCTION")

#####################################################################

#4

number = int(input("What number do you want displayed? (1-6)   "))

if number == 1:
    
    print("    oooooooooooo")
    print("    o          o")
    print("    o          o")
    print("    o     #    o")
    print("    o          o")
    print("    o          o")
    print("    oooooooooooo")

elif number == 2:

    print("    oooooooooooo")
    print("    o          o")
    print("    o   #      o")
    print("    o          o")
    print("    o       #  o")
    print("    o          o")
    print("    oooooooooooo")

elif number == 3:
    print("    oooooooooooo")
    print("    o          o")
    print("    o  #       o")
    print("    o     #    o")
    print("    o       #  o")
    print("    o          o")
    print("    oooooooooooo")
elif number == 4:
    print("    oooooooooooo")
    print("    o          o")
    print("    o  #    #  o")
    print("    o          o")
    print("    o  #    #  o")
    print("    o          o")
    print("    oooooooooooo")
elif number == 5:
    print("    oooooooooooo")
    print("    o          o")
    print("    o  #    #  o")
    print("    o     #    o")
    print("    o  #    #  o")
    print("    o          o")
    print("    oooooooooooo")
else:
    print("    oooooooooooo")
    print("    o          o")
    print("    o  #    #  o")
    print("    o  #    #  o")
    print("    o  #    #  o")
    print("    o          o")
    print("    oooooooooooo")

#####################################################################

#5

number1 = int(input("What is the first number?:   "))
number2 = int(input("What is the second number?:   "))

if number1 < number2:
    print(number2)
else:
    print(number1)

#####################################################################

#5

nitrateLevel = int(input("what is the nitrate level?  "))

if nitrateLevel > 10:
    print("3 mL dose")
elif nitrateLevel > 2.5:
    print("Dose 2mL")
elif nitrateLevel > 1:
    print("dose 1mL")
else:
    print("Dose 0.5 mL")

#####################################################################

#6

analysisScore = int(input("What is the score for you analysis grade band?   "))
designScore = int(input("What is the score for you  design grade band?   "))
implementationScore = int(input("What is the score for you  implementation grade band?   "))
evaluationScore = int(input("What is the score for you  evaluation grade band?   "))

overallScore = (analysisScore+designScore+implementationScore+evaluationScore)/4

if  4> overallScore:
    print("U is your score")
    pointsAway = 13-overallScore
elif  13> overallScore >=4 :
    print("G is your score")
    pointsAway = 22-overallScore
elif  22> overallScore >=13 :
    print("F is your score")
    pointsAway = 31-overallScore
elif  31> overallScore >=22 :
    print("E is your score")
    pointsAway = 41-overallScore
elif  41> overallScore >=31 :
    print("D is your score")
    pointsAway = 54-overallScore
elif  54> overallScore >=41 :
    print("C is your score")
    pointsAway = 67-overallScore
elif  67> overallScore >=54 :
    print("B is your score")
    pointsAway = 80-overallScore
elif  80> overallScore >= 67:
    print("A is your score")
elif  overallScore >=80 :
    print("A* is your score. Congrats")

#####################################################################

#7

balance = "$ 1,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000"

withrawl = int(input("How much would you like to withdrawl?"))
withrawl = round(withrawl/10)*10

balance = balance - withrawl

if withrawl > 250:
    print("you're too gready. You'll only get $250")
    withrawl=250
    if withrawl%20==0:
        twenties = withrawl/20
        print("Youll get ",twenties," $20 bills")
    else:
        withrawl=withrawl-10
        twenties = withrawl/20
        print("Youll get ",twenties," $20 bills and 1 $10 bill")
else:
    if withrawl%20==0:
        twenties = withrawl/20
        print("Youll get ",twenties," $20 bills")
    else:
        withrawl=withrawl-10
        twenties = withrawl/20
        print("Youll get ",twenties," $20 bills and 1 $10 bill")

print("Your balance is now ", balance)

#####################################################################

#8

element = input("What is the elements?   ").lower()

if element == "hydrogen" or element == "h":
    print("H, Hydrogen, 1.01")
elif element == "Llithium" or element == "li":
    print("Li, Lithium, 6.94")
elif element == "oxygen" or element == "o":
    print("O, Oxygen, 16.0")
elif element == "zinc" or element == "zn":
    print("Zn, Zinc, 65.4")
elif element == "nitrogen" or element == "n":
    print("N, Nitrogen, 14.0")
elif element == "he" or element == "helium":
    print("He, Helium, 4.0")
else: 
    print("sorry. we dont have this element i our databse yet")

#####################################################################

#9

stations = int(input("number of stations   "))
ogStations = stations
adults = int(input("Number of adults   "))
kids = int(input("Number of chidren   "))
timeDay = int(input("Time of Day   (mlitary time)"))

stations = stations*20
if 600 <= timeDay <= 900:

    stations = stations + ogStations*5

money = adults*stations + (kids*stations)/2

print("$",money)

#####################################################################

#10

# Write a program that asks the user for the number of hours worked this week and their hourly rate of pay.
# The program is to calculate the gross pay. If the number of hours worked is greater than 40, the extra
# hours are paid at 1.5 times the rate. The program should display an error message if the number of hours
# worked is not in the range 0 to 60.

hourlyRate = int(input("Hourly rate   "))
timeWroked = int(input("Time worked this week   (hours)"))

if 0 <= timeWroked <= 60:
    if timeWroked > 40:
        over40 = timeWroked-40
        under40 = timeWroked-over40
        monkey = under40*hourlyRate + over40*hourlyRate*1.5
        print("You earned $",monkey)
else:
    print("error in time worked")