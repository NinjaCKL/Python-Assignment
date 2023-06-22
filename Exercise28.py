class Person:
    def __init__(self, name_para, age_para):
        self.name = name_para
        self.age = age_para
    def __str__(self):
        return f"Name: {self.name} and Age: {self.age}"
    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."
class Student(Person):
    major = ''
    studentID = ''
    def showInfo(self):
        print(f"Student name: {self.name} \nID: {self.studentID} \nMajor: {self.major}")

costStudent = Student('Chea Kimleang', '21')
costStudent.major = 'Information Technology'
costStudent.studentID = '603656'

print(costStudent.greet())
costStudent.showInfo()