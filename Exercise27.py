#Chea Kimleang 60-19-05-79

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
myClassmate = Person("Chea Kimleang", 21)

print(myClassmate.name)
print(myClassmate.age)
myClassmate.greet()