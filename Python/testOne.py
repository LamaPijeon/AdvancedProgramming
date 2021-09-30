import os
os.system("clear")

# Please type your name here: Patryk Nowak
# 
#
# This is a programming test. The purpose of this test is to assess your knowledge and skill of
# basic programming.  

#-------------------
# Academic integrity
#-------------------

# By typing your full name below  you hereby declare that the answers on this assessment 
# are representative of your own learning and not that of others.
# Type your full name here -->  Patryk Nowak


# By typing your full name below you declare you have individually maintained 
# a level of confidentiality and personal ownership of your own work.
# Type your full name here --> Patryk Nowak




# Answer each question as best as you can. Make sure your work is your own.
# Please type your answer under each question.  If you do not know an answer, please make your best guess. 
# You are only allowed to use a python cheat sheet which will be provided to you. 
# You are not allowed to have a browser open. You are not allowed to any other tabs open on vscode 
# other than this file. You must have the vscode file explorer closed. When you are done with this 
# test send an email to bmackenty@aswarsaw.org with the completed quiz attached to the email.

# Good luck! 


 
# Question 1: Match the data types by copying / pasting the data type example next to the correct datatype.


# Boolean :	False					

# Integer	:	42				

# Float		:	10.01				

# String	:	“Hello World”				




# Question 2: State the result of the following operation: 

# 4 + 4 
# 8


# Question 3: State the result of the following operation:

# 4 * 4
# 16


# Question 4: State the result of the following operation:

# 16 / 4
#4


# Question 4: State the result of the following operation:

# 18%3
#0



# Question 5: State the result of the following operation:

# 4 ** 2

#16


# Question 6: Consider the string below and answer the following questions. 

# my_secret_password = “password1234”

# 6a.  State the ouput of: my_secret_password[0] --> "p"

# 6b. State the ouput of: my_secret_password[4] --> "w"

# 6c. State the ouput of: my_secret_password[2:5] --> "ssw"




# Question 7: State the result of the following code:

# my_food=”chocolate”
# if my_food != “vanilla”:
#     print(“A”)
# else:
#     print(“B”)

#if your food is not equal to "vanilla," It will print "A" in the terminal. If it's "vanilla" it will print "B" in console


# Question 8: Construct a program that allows the user to input the name of two cities. 
# The program should then output the first 3 characters of each city in capital letters, 
# separated by a dash. For example, the input London & Madrid would output LON-MAD

city1 = input("What is the first city?  ")
city2 = input("What is the second city?  ")
city1 = city1[0:3].upper()
city2 = city2[0:3].upper()

print(city1,"-",city2)




# Question 9: Construct a program that asks the user for two numbers, adds them together and 
# outputs the answer. For example: You entered numbers 5 and 12 They add up to 17.

number1 = float(input("What's the first number?   "))
number2 = float(("What's the second number?   "))

print(number1+number2)

# Question 10: What exception or error will this program create when it is executed?


# user_name = int(“Enter your name: “)
# print(“Hello, “, user_name)

#ValueError: could not convert string to int: “Enter your name: “
#since "Enter your name: " is a string, it can't be converted into an integer.



# # Grading Scheme
# # Grade: 1
# # No knowledge or understanding of the relevant issues and concepts.


# # Grade: 3
# # Minimal knowledge and understanding of the relevant issues or concepts.


# # Grade: 5
# # Responses with knowledge and understanding of the relevant issues and/or concepts.


# # Grade: 7
# # Responses with detailed knowledge and clear understanding of the relevant issues and/or concepts.