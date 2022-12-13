class Person:
    def __init__ (dharm,name,surname,emailid,year_of_birth):
        dharm.name = name
        dharm.surname=surname
        dharm.emailid=emailid
        dharm.year_of_birth=year_of_birth

anuj_var= Person("anuj","bhandari","bandari@gmail.com",1983)
Dharmendra = Person("Dharmendra", "Kantharia", "dk@gmail.com", 1984)

print(anuj_var.name)
print(anuj_var.surname)
print(anuj_var.emailid)
print(anuj_var.year_of_birth)

# concatination of name and surname
print(Dharmendra.name + Dharmendra.surname)
print(Dharmendra.name)
print(Dharmendra.surname)
print(Dharmendra.emailid)
print(Dharmendra.year_of_birth)