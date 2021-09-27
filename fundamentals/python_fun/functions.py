def printMultiplesOfthree(startNum, stopNum):
    if(stopNum<startNum):
        print("stop playin' give a larger stop num. aintnobodygottimeforthat")
        return False
    for i in range(startNum, stopNum, 3):
        print(i)
    print("function completed running")

# printMultiplesOfthree(10,5)
# printMultiplesOfthree(stopNum=10,startNum=5)
# printMultiplesOfthree(2,20)
# printMultiplesOfthree(25,20)




def add(a,b):	# function name: 'add', parameters: a and b
    x = a + b	# process
    print("finished calculating")
    return x

#THE VALUE OF A FUNCTION CALL IS WHATEVER THAT FUNCTION CALL RETURNS


# result = add(5,10)
# print(result)

# print(add(5,10))
# youngmoney = add(10,3) + add(2,8)
# print(youngmoney)



def greetSomebody(sport, name="Student"):
    # return "Hello " + name + ". Nice to meet you!"
    return f"Hello {name}. Nice to meet you! Lets play some {sport}"


print(greetSomebody(sport="Basketball", name="Oliver"))
# print(greetSomebody("Matthew"))
# print(greetSomebody())

