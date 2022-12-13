class Person:
    def __init__ (self,name,surname,yob):
        # When ever we use "-" in front of any variable it means variable in public.
        # when ever we use "_ _" in front of any variable it means variable in protected or privat variable.To access the protected variable use "_ with class name" for Example: this is code our class is _Person
        self._name1 = name
        self.__surname1 = surname
        self.yob1 = yob

dharam = Person("Dharmendra","Kantharia",1983)
print(dharam._name1)
print(dharam._Person__surname1) # __ means private to use private variable use _ with class