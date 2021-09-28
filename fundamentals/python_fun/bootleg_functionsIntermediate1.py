x = [ "hello",300,[15,12,13], [10,[40,50],9], [3,6,9] ] 



# Change the value 12 in x to 15. 
# print(x[2][1])
# x[2][1]= 15
# print(x)


# Change the value 40 in x to 400. 
# print(x[3][1][0])
# x[3][1][0]=400
# print(x)



pets = [
     {'name':  'Junior', 'age' : 3, 'type': 'Dog'},
     {'name' : 'Fluffy', 'age' : 10, 'type': 'Cat'}
]

sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'a': 100, 'b': 200}, {'name': "Weezy", 'age': 38} ]

# Change the type of the first pet from 'Dog' to 'Alpaca'
# print(pets[0]['type'])
# pets[0]['type']= "Alpaca"
# print(pets)


# In the sports_directory, change 'Curry' to 'Johnson'
# print(sports_directory["basketball"][3])
# sports_directory["basketball"][3]= "Johnson"
# print(sports_directory)

# Change the value 20 in z to 30
# print(z[0]['b'])
# z[0]['b']= 300
# print(z)




food = [
         {'name':  'Calamari', 'calories' : 300},
         {'name' : 'Sweet Potato', 'calories' : 100},
         {'name' : 'Apple', 'calories' : 50},
         {'name' : 'Pasta', 'calories' : 500}
    ]

# Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value.

def iterateDictionary(some_list):
    # print(some_list)
    # result = ""
    for i in range(0, len(some_list), 1):
        print(f"name-{some_list[i]['name']}")
        print(f"calories-{some_list[i]['calories']}")
        # result += f"name-{some_list[i]['name']}, calories-{some_list[i]['calories']}\n "

    # print(result)


# iterateDictionary(food)



# iterateDictionary(food) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
# name - Calamari, calories - 300
# name - Sweet Potato, calories - 100
# name - Apple, calories - 50
# name - Pasta, calories - 500





# Create a function iterateDictionary2(key_name, some_list) that, given a list of dictionaries and a key name, the function prints the value stored in that key for each dictionary.
food2 = [
         {'name':  'Calamari', 'calories' : 300},
         {'name' : 'Sweet Potato', 'calories' : 100},
         {'name' : 'Apple', 'calories' : 50},
         {'name' : 'Pasta', 'calories' : 500}
    ]

def iteratedictionary2(key_name, some_list):
    for i in range(0, len(some_list), 1):
        print(some_list[i][key_name])


# iteratedictionary2("name", food2)


finance = {
   'crypto': ['Bitcoin', 'Etherum', 'Cardano', 'ChainLink', 'Dogecoin'],
   'stock': ['Apple', 'Tesla', 'Microsoft', 'Amazon', 'AirBnB', 'Google', 'AMC', 'Gamestop', 'Square']
}

def printInfo(someDictionary):
    # print(someDictionary)
    for key in someDictionary:
        print(len(someDictionary[key]),key.upper())
        for value in someDictionary[key]:
            print(value)

printInfo(finance)

# printInfo(dojo)
# # output:

# 5 CRYPTO
# Bitcoin
# Etherum
# Cardano
# ChainLink
# Dogecoin

    
# 9 STOCK
# Apple
# Tesla
# Microsoft
# Amazon
# AirBnB
# Google
# AMC
# Gamestop
# Square
