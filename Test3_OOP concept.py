class Person:

    def age(self,current_year,year_of_birth):
        return current_year - year_of_birth

    def email_id_input(self,email_id):
        print("Take and mail id from a person and print it",email_id)

    def ask_name(self):
        name = input("tell me your name")
        return name

    def ask_dob(self):
        dob = input("tell me your dob")
        return dob
    
Dharmendra =Person()
Kantharia =Person()
Renuka = Person()

Dharmendra.email_id_input("Dk@gmail.com")
print(Dharmendra.ask_name())
