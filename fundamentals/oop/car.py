class Car:
    def __init__(self,makeInput):
        self.make = makeInput
        self.totalGallonsInTank = 20

    def driveCar(self, numMiles):
        if(self.totalGallonsInTank> numMiles):
            self.totalGallonsInTank-=numMiles
        else:
            print("this is not the hitchhikers guide to the galaxy, in other word, fill up that tank tho")
        return self
    
    def pumpGasForCar(self, numGallons):
        self.totalGallonsInTank+= numGallons
        return self
    
    def displayCarInfo(self):
        # print(f"Car make: {self.make} \n Number of gallons left: {self.totalGallonsInTank}")
        return f"Car make: {self.make} \n Number of gallons left: {self.totalGallonsInTank}"


car1 = Car("Ford")
car2 = Car("Mazarati")
car3 = Car("Honda")

# car1.displayInfo()
# car2.displayInfo()
# car1.drive(5).displayInfo()




    
