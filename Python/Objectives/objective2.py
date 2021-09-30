# # Name & Age

# print()
# name = input("What's Your Name?:     ")
# print()
# age = int(input("How old are you?:      "))
# print()
# print()

# print("Hello ", name, ", you are ", age, " years old. I'm so smart.")
# print()

# ###############################################################################################

# # 2 Number Adder


# a = int(input("First Number: "))
# print()
# b = int(input("Second Number: "))
# print()
# print(a+b)
# print()

# ###############################################################################################

# # 3 test score average


# test1 = int(input("First Test Score (out of 100): "))
# print()
# test2 = int(input("Second Test Score (out of 100): "))
# print()
# test3 = int(input("Third Test Score (out of 100): "))
# print()

# average = (test1+test2+test3)/3

# print("The average score of these tests was ",average,"/100")
# print()

# ###############################################################################################

# # Celcuis & Fahreinheit converter

# print()

# chosenTemp = input("Degrese in Centigrade or Fahrenheit? (c or f) ")
# print()

# if chosenTemp == "f":

#     chosenTemp = int(input("What is the temperature in Fahrenheit: "))
#     result = (chosenTemp - 32) * (5/9)
#     solution = "Centigrade"

# elif chosenTemp == "c":

#     chosenTemp = int(input("What is the temperature in Celntigrade: "))
#     result = (chosenTemp * (9/5)) + 32 
#     solution = "Fahrenheit"

# else:
#     print()

#     print("You have not typed in a correct letter (c or f). make sure they aren't capatalized")

# print()

# print("The conversion is ", result, "degrees ",solution)
# print()

# ###############################################################################################

# # Stongs & Inches to KG & cm

# print()

# weightStones = int(input("weight in stones: "))
# print()
# heightInches = int(input("height in inches: "))
# print()

# weightKilo = weightStones*6.364
# heightCm = heightInches*2.54 

# print("Your height is ",heightCm,"cm and you weigh ",weightKilo,"kg")
# print()

# ###############################################################################################

# # Wage of worker (toys&hours)

# print()

# toys = int(input("how many toys have you made: "))
# print()
# hours = int(input("How many hours have you worked: "))

# wage = hours*9 + toys*.6
# print()

# print("you made  £",wage," today")
# print()

# ###############################################################################################

# # Tank volume & Surface Area

# print()
# width = int(input("What is the width of the tank? (in cm):    "))
# print()
# height = int(input("What is the height of the tank? (in cm):   "))
# print()
# depth = int(input("What is the depth of the tank? (in cm):    "))

# tankVolumeCm = width*height*depth
# tankVolume = tankVolumeCm/1000
# surfaceArea = 2*(width * height) + 2*(height * depth) + 2*(width * depth)

# print()
# print()
# print()

# print("The volume of your tank is ", tankVolume, " Liters")
# print()
# print("The surface area of your tank is ", surfaceArea, " cm^2")
# print()

###############################################################################################

# Circle Problem
print()
circleDi = int(input("What is the diamater of the circle:  "))
print()
arc = int(input("What is the measure of the arc angle:   "))
print()
units = input("Is this in radians or degrees (r or d):   ")
print()
degrees = arc

if units == "r":
    degrees = arc * 180/3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912

radius = circleDi/2
circumfrance = 3.14*circleDi
area = 3.14159265358979323846264338327950288419716939937510582097494459230781640628620899862803482534211706798214808651328230664709384460955058223172535940812848111745028410270193852110555964462294895493038196442881097566593344612847564823378678316527120190914564856692346034861045432664821339360726024914127372458700660631558817488152092096282925409171536436789259036001133053054882046652138414695194151160943305727036575959195309218611738193261179310511854807446237996274956735188575272489122793818301194912*radius**2
arcLen = circumfrance*degrees/360

print()
print("The radius of this circle is:  ",radius," units")
print()
print("The circumfrance of this circle is:  ",circumfrance," units")
print()
print("The area of this circle is:  ",area," units^2")
print()
print("The arc length of this circle is:  ", arcLen," units")
print()