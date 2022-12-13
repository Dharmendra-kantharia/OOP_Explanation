class Person:
    def __init__ (self,name,surname,emailid,year_of_birth):
        self.name = name
        self.surname=surname
        self.emailid=emailid
        self.year_of_birth=year_of_birth

    def age(self,current_year):
        return current_year - self.year_of_birth

anuj_var= Person("anuj","bhandari","bandari@gmail.com",1983)
Dharmendra = Person("Dharmendra", "Kantharia", "dk@gmail.com", 1984)

print(anuj_var.name)
print(anuj_var.surname)
print(anuj_var.emailid)
print(anuj_var.year_of_birth)

print(Dharmendra.name)
print(Dharmendra.surname)
print(Dharmendra.emailid)
print(Dharmendra.year_of_birth)
print(anuj_var.age(2022))
print(Dharmendra.age(2022))

