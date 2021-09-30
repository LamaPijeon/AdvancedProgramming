# # 1

# name = input("What is your name:  ")

# locationOfSpace = name.find(" ")+1
# firstInitial = name[0].upper()
# lastName = name[locationOfSpace:].upper()

# print(firstInitial, lastName)

# #######################################################################

# # 2

# cities = input("What are the two cities:   ")

# spaceLocation = cities.find(" ")

# firstCity = cities[:spaceLocation]
# firstCity = firstCity[0:4].upper()
# secondCity = cities[spaceLocation+1:]
# secondCity = secondCity[0:4].upper()

# print(firstCity,"-",secondCity)

# #######################################################################

# # 3

# name = input("What is your name:   ")

# spaceLocation = name.find(" ")

# firstName = name[:spaceLocation]
# lastName = name[spaceLocation:]

# print("First Name : ",firstName)
# print("Last Name : ",lastName)

#######################################################################

# 4.1

# phrase = "Quick brown fox jumps over the lazy dog"
# phraseLower = phrase.lower()

# print(phrase)
# print()

# deleteWord = input("Which word would you like to remove?: ")

# wordLocation = phraseLower.find(deleteWord)

# wordEnd = phraseLower[wordLocation:].find(" ")
# wordEnd = wordEnd+wordLocation

# beginningWord = phrase[:wordLocation]
# endWord = phrase[wordEnd:]

# print()
# print(beginningWord, endWord)
# print()

#######################################################################

# 4.2

# phrase = "Quick brown fox jumps over the lazy dog"
# phraseLower = phrase.lower()

# print(phrase)
# print()

# phrase = phrase.replace(input("Which word would you like to remove?: "), "")



# print()
# print(phrase)
# print()
