class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def print_person(person):
    match person:
        case Person(name="Tom", age=37):
            print("Default Person")
        case Person(name=name, age=37):
            print(f"Name: {name}")
        case Person(name="Tom", age=age):
            print(f"Age: {age}")
        case Person(name=name, age=age):
            print(f"Name: {name}  Age: {age}")


print_person(Person("Tom", 37))  # Default person
print_person(Person("Tom", 22))  # Age: 22
print_person(Person("Sam", 37))  # Name: Sam
print_person(Person("Bob", 41))  # Name: Bob  Age: 41


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
 
class Student:
    def __init__(self, name):
        self.name = name
 
 
def print_person(person):
    match person:
        case Person(name="Tom") | Student(name="Tomas"):
            print("Default Person/Student")
        case Person(name=name) | Student(name=name):    # получаем только атрибут name
            print(f"Name: {name}")
        case _:
            print("Not a Person or Student")
 
 
print_person(Person("Tom", 37))     # Default Person/Student
print_person(Student("Tomas"))      # Default Person/Student
 
 
print_person(Person("Bob", 41))     # Name: Bob
print_person(Student("Mike"))       # Name: Mike
 
print_person("Tom")                 # Not a Person or Student


class Person:
    __match_args__ = ("name", "age")
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
 
def print_person(person):
    match person:
        case Person("Tom", 37):
            print("Default Person")
        case Person(person_name, 37):
            print(f"Name: {person_name}")
        case Person("Tom", person_age):
            print(f"Age: {person_age}")
        case Person(person_name, person_age):
            print(f"Name: {person_name}  Age: {person_age}")
 
 
print_person(Person("Tom", 37))  # Default person
print_person(Person("Tom", 22))  # Age: 22
print_person(Person("Sam", 37))  # Name: Sam
print_person(Person("Bob", 41))  # Name: Bob  Age: 41
