# Exercise 1 : Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
class vehicle:
    color = "White"
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self,capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

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

# Exercise 4: Class Inheritance
#             Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.

class Bus(vehicle):
    def seating_capacity(self,capacity = 55):
        return super().seating_capacity(capacity=55)

school_bus = Bus("School volvo",180,20)
print(school_bus.seating_capacity())

# Exercise 5: Define a property that must have the same value for every class instance (object)
#             Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.

class vehicle:
    color = "White"
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(vehicle):
    pass

class Car(vehicle):
    pass

School_bus = Bus("School Volvo", 180, 12)
print(School_bus.color, School_bus.name, "Speed:", School_bus.max_speed, "Mileage:", School_bus.mileage)

car = Car("Audi Q5", 240, 18)
print(car.color, car.name, "Speed:", car.max_speed, "Mileage:", car.mileage)

# Exercise 6: Class Inheritance
#             Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. 
#             If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will become 
#             the final amount = total fare + 10% of the total fare.

class vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        return self.capacity * 100

class Bus(vehicle):
    def fare(self):
        amount = super().fare()
        amount += amount * 10 / 100
        return amount

School_bus = Bus("School Volvo", 12, 50)
print("Total Bus fare is:", School_bus.fare())

# Exercise 7: Check type of an object
#             Write a program to determine which class a given Bus object belongs to.

class vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

# Python's built-in type()
print(type(School_bus))

# Exercise 8: Determine if School_bus is also an instance of the Vehicle class

class vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(vehicle):
    pass

School_bus = Bus("School Volvo", 12, 50)

# Python's built-in isinstance() function
print(isinstance(School_bus, vehicle))

