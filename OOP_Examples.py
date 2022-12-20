# Exercise 1 : Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self,capacity):
        return f"The seating capacity of a {self.name} is {capacity}passengers"

obj = vehicle("Student : Dharmendra",240,18)
print(obj.name,obj.max_speed,obj.mileage)

# Exercise 2: Create a Vehicle class without any variables and methods

class vehicle1:
    pass

# Exercise 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Bus(vehicle):
        pass
obj1 = Bus("School vachicle:volvo","Speed:180","Mileage:12")
print(obj1.name,obj1.max_speed,obj1.mileage)
print(obj.seating_capacity(50))



