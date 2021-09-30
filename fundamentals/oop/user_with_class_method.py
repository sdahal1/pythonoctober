import car


class User:
    maxCaloriesAllowedToConsume = 2000
    def __init__(self,nameInput, emailInput, ageInput): 
        self.name = nameInput
        self.email = emailInput
        self.age = ageInput
        self.totalCalories = 0
        self.totalGallonsInTank = 20
        self.workCar = car.Car("Ford")
        self.familyCar = car.Car("Mazeradi")

    def eat(self, numCalories):
        if(numCalories < User.maxCaloriesAllowedToConsume):
            print("woah there young blood, thats cheese cake bruleee factory or whats good wit you. Insulin spike be cray cray. basically go exercise foo")
            return self
        else:
            print(f"{self.name} is eating")
            self.totalCalories+= numCalories
            return self
    
    def exercise(self, numCalories):
        print(f"{self.name} is exercising")
        if(self.totalCalories< numCalories):
            print(f"you havent consumed enough calories to exercise that much. Your have this many total calories: {self.totalCalories} and you are trying to burn this many calories: {numCalories}")
        else:
            self.totalCalories-= numCalories
        return self

    def drive(self, numMiles, chosenCar):
        if(chosenCar=="work"):
            self.workCar.driveCar(numMiles)
        else:
            self.familyCar.driveCar(numMiles)
        return self
    
    def pumpGas(self, numGallons, chosenCar):
        if(chosenCar=="work"):
            self.workCar.pumpGasForCar(numGallons)
        else:
            self.familyCar.pumpGasForCar(numGallons)
        return self

    def displayInfo(self):
        print(f"Your stats: \n Name: {self.name} \n Email: {self.email} \n Age: {self.age} \n Total Calories: {self.totalCalories} \n Work car: {self.workCar.displayCarInfo()} \n Family Car: {self.familyCar.displayCarInfo()}")
        return self

    @classmethod
    def change_max_calorie_allowed(cls, newAmount):
        cls.maxCaloriesAllowedToConsume = newAmount


#creating OBJECTS here--> an object is an instance of a class
user1 = User("Rob", "rob@gmail.com", 29)
user2 = User("Larry", "larry@gmail.com", 74)




