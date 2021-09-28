#think of the class User as a BLUEPRINT--> a set of instructions to create many instances from
class User:
    def __init__(self,nameInput, emailInput, ageInput): #this is the __init__ method (a method is just a function that belongs inside a class)
        #name, email, age, and totalCalories are ATTRIBUTES
        self.name = nameInput
        self.email = emailInput
        self.age = ageInput
        self.totalCalories = 0

    def eat(self, numCalories):
        print(f"{self.name} is eating")
        self.totalCalories+= numCalories
    
    def exercise(self, numCalories):
        print(f"{self.name} is exercising")
        if(self.totalCalories< numCalories):
            print(f"you havent consumed enough calories to exercise that much. Your have this many total calories: {self.totalCalories} and you are trying to burn this many calories: {numCalories}")
        else:
            self.totalCalories-= numCalories
    
    def displayInfo(self):
        print(f"Your stats: \n Name: {self.name} \n Email: {self.email} \n Age: {self.age} \n Total Calories: {self.totalCalories}")


#creating OBJECTS here--> an object is an instance of a class
user1 = User("Rob", "rob@gmail.com", 29)
user2 = User("Larry", "larry@gmail.com", 74)

user1.eat(1000)
user2.eat(75)
user1.exercise(300)
user2.exercise(100)

user1.displayInfo()
user2.displayInfo()
# user1.totalCalories += 200
# user2.totalCalories +=500
# print("user 1 just ate 200 calories worth of food")

# print(user1.totalCalories) #200
# print(user2.totalCalories) #500



