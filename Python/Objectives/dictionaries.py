# The code below creates a dictionary 
# Please note the KEY:VALUE construction

studentEmail = {
'Alice':'alice@google.com', 
'Bob':'bob@facebook.com', 
'Charlie':'charlez@microsoft.com', 
'Daniel':'danny@aswarsaw.org'
}

# Bob's email can be called by:

studentEmail['Bob']

# (in a list, we would need to do something like: studentEmail[1] )

# If you want to print a dictionary (kind of ugly) you can simply type:

print(studentEmail)

# However, it is far more common to retrieve an element by it's key
# The instructions below accesses Bob's email address:

print(studentEmail['Bob'])

# in addition, we have the following functions to access elements in a dictionary<ref>https://www.digitalocean.com/community/tutorials/understanding-dictionaries-in-python-3</ref>:

# dict.keys() isolates keys
# dict.values() isolates values
# dict.items() returns items in a list format of (key, value) tuple pairs
# if we want to add into a dictionary we can simply type:

studentEmail['Bill'] = 'bmackenty@aswarsaw.org'

# if we wanted to replace a certain element, we could simply overwrite it. 

studentEmail['Bill'] = 'bmackenty@gmail.com'

# The del function deletes an element from a list:

del studentEmail['Bill']

studentEmail = {
'Alice':'alice@google.com', 
'Bob':'bob@facebook.com', 
'Charlie':'charlez@microsoft.com', 
'Daniel':'danny@aswarsaw.org'
}

# iterate through the keys:
for i in studentEmail.keys():
    print(i)

# iterate through the values:
for i in studentEmail.values():
    print(i)

# iterate through the items:
for i in studentEmail.items():
    print(i)   

# to test if a key is in a dictionary
if "Alice" in studentEmail:
    print("Alice is in the dictionary")
else:
    print("Alice is not in the dictionary")

# to test if a value is in a dictionary
if "alice@google.com" in studentEmail.values():
    print("alice@google.com is in the dictionary")
else:
    print("alice@google.com is not in the dictionary")

# if we want to get the key from a value, this is one way to do it. 
for key, value in studentEmail.items():
    if value == "alice@google.com":
        print(key)