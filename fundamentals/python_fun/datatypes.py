import random





usaBasketballWonGold= True


# print(greeting)
# print(whatRobdoes)
# print(whatRobReallyDoes)
# print(usaBasketballWonGold)

#numbers
num_gold_medals = 6 #data type is int--> this is a whole number
world_record100m = 9.58888 #data type is float --> this is a decimal numer

# print(type(num_gold_medals))
# print(float(world_record100m))

# print(float(num_gold_medals))
# print(int(world_record100m))

# print("random number is this",random.randint(2,5))



#strings
greeting = "hello everyone!"
whatRobdoes ="i keep it 100"
whatRobReallyDoes= 'i really do be keeping it 100 tho'

print(len("this is a sample string"))
print(len(greeting))
print(greeting[len(greeting)-1])


#string are immutable--> meaning i cannot modify existing values in the string
# greeting[0] = "H"

x = "400"
y= int(x)
print(y) 

name = "Oliver"

#concatenation of strings 
print("Hi my name is", name) #using comma
print("Hi my name is "+ name) #using a plus operator


current_year = 2021
favfood = "Calamari"
print("the current year is", current_year,"and my favorite food is" , favfood)
print("the current year is " + str(current_year) + " and my favorite food is " + favfood) #the current year is 2021 and my favorite food is Calamari


#fstring way to concat strings
print(f"the current year is {current_year} and my favorite food is {favfood}")

#.format() way to concat strings
print("the current year is {} and my favorite food is {}".format(current_year, favfood))




















