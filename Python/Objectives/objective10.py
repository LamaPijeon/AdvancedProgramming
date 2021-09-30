import random
# #1 Quote of the day
# with open('Text Files/quoteOfTheDay.txt', 'r') as f:

#     f_contents = f.read()
#     print(f_contents)

# #2 Quote of the day challenge 2
# with open('Text Files/quoteOfTheDay.txt', 'r') as f:
#     f_list = f.readlines()
#     lineNum = [random.randint(1,len(f_list))-1]
#     print(lineNum)
#     for position, line in enumerate(f_list):
#         if position in lineNum:
#             print(line)

# # 3 Product catalogue challenge

# price = float(input("What's the price :  "))
# description = input("What's the description :  ")
# code = float(input("What's the code :  "))

# with open('Text files/catalog.txt','a') as catalog:
#     item = [str(price),str(description),str(code)]
#     catalog.write(str(item) + "\n")

# # 4 Product catalogue challenge.2
# code = " "
# while code != "":
#     price = float(input("What's the price :  "))
#     description = input("What's the description :  ")
#     code = (input("What's the code :  "))
#     if code != "":
#         with open('Text files/catalog.txt','a') as catalog:
#             item = [str(price),str(description),str(code)]
#             catalog.write(str(item) + "\n")

# # 5 Product catalogue challenge.3

# code = " "

# while code != "":
#     what = input("Add Product, check catalog, close program (add, check, close) :  ").lower()
#     if what == "add":
#         price = float(input("What's the price :  "))
#         description = input("What's the description :  ")
#         code = (input("What's the code :  "))
#         with open('Text files/catalog.txt','a') as catalog:
#             item = [str(price),str(description),str(code)]
#             catalog.write("\n"+str(item))

#     elif what == "check":
#         with open('Text files/catalog.txt','r') as catalog:
#             for line in catalog:
#                 print(line, end='')
#             print()

#     elif what == "close":
#         code = ""

# 6 Quiz challenge