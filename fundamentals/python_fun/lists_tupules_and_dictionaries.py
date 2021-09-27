ninjas = ['Rozen', 'KB', 'Oliver']
my_list = ['4', ['list', 'in', 'a', 'list'], 987]
moreNinjas = ["Larry David", "Dave Chappelle", "Harold and Kumar go to White Castle"]


# print(ninjas[1])
# ninjas[1] = "Kobe"
# print(ninjas)

# ninjas.append("Iverson")
# print(ninjas)
# removedPerson = ninjas.pop()
# print("just did the .pop() operation")
# print(ninjas)
# print(removedPerson)

# combinedNinjas = ninjas + moreNinjas
# print(combinedNinjas)

# multipliedNinjas = ninjas *3
# print(multipliedNinjas)


daysOfWeek = ("Monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday") 

# print(daysOfWeek[0])
# daysOfWeek.append("day 8") #cannot append to tupule and cannot modify a tupule
# daysOfWeek.pop() #cannot append to tupule and cannot modify a tupule





#dictionaries
person1 = {
    "first_name": "Benjamin",
    "last_name": "Duso",
    "num_belts": 1,
    "plays_pingpong": True,
    "fav_movies": ["Inglorious Bs", "Pacific Rim", "Revenge of the Sith"]
}
print(person1)
person1["first_name"]= "Ben"
print(person1)
person1["location"]= "Massachusetts"
print(person1)


poppedvalue = person1.pop("first_name")
print(person1)
person1["name"] = poppedvalue
print(person1)















