dessert = None

def add_2(number):
    global dessert
    print(dessert)
    return number + 2


dessert = "pie"
for count in range(0,12):
    print(add_2(count))
