
import Test1_OOP_concept # <-- To import other file variable in this file.
# from Test1 import Person1 <-- If we want to import only one class from other file use this
print(Test1_OOP_concept)

# OOP Inheritance concept (Inheritance means we can use our parent class in other class)

# Parent Class
class Person: # <--This is my class-1 Parent class. 

    #Here we are not using __init__ constructor because we are not passing any data.

    _name = "Dharmendra" #<--Variable is public
    __surname = "Kantharia" #<--Variable is private
    Yob = 1983

    def _age (self,current_year):
        return(current_year - self.Yob)

    def __age (self,current_year):
        return(current_year - self.Yob)  

obj = Person() # <-- Object of the class
print(obj)
print(obj._age(2022))
print(obj._Person__age(2022))

# Child class
class employee(Person): #<--This is my class-2.To use class-1 in class-2 wirte class-1 name in bracket. Exm:(Person).
    pass

obj1 = employee() # <-- Object of the class
print(obj1)
print(obj1.Yob) # <-- Here we can see and access the variable of our class-1 (Parent class)
print(obj1._name) # <-- Here we can see and access the variable of our class-1 (Parent class)
print(obj1._Person__surname)