#Python Object Oriented Programming (OOP) - For Beginners
#https://www.youtube.com/watch?v=JeznW_7DlB0

# - EXEMPLE 01 - - - - - - - - - - - - - - - - #
print('\n# - EXEMPLE 01 - - - - - - - - - - - - - - - - #\n')

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def add_one(self,x):
        return x+1

    def bark(self):
        print("bark")

    def set_age(self,age):
        self.age = age

dog = Dog("Tim",34)
dog.set_age(23)
print(dog.get_age())

dog2 = Dog("Bill",12)

# - EXEMPLE 02 - - - - - - - - - - - - - - - - #
print('\n# - EXEMPLE 02 - - - - - - - - - - - - - - - - #\n')

class Student:
    def __init__ (self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def get_grade(self):
        return self.grade
class Course:
    def __init__ (self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        return False
    
    def get_average_grade(self):
        value = 0
        for student in self.students:
            value += student.get_grade()

        return value / len(self.students)

s1 = Student("Tim", 19, 95)
s2 = Student("Bill", 19, 75)
s3 = Student("Jill", 19, 65)

course = Course("Science", 2)
course.add_student(s1)
course.add_student(s2)
print(course.get_average_grade())
print(course.students[0].name)


# - EXEMPLE 03 - - - - - - - - - - - - - - - - #
print('\n# - EXEMPLE 03 - - - - - - - - - - - - - - - - #\n')

class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    
    def speak(self):
        print("AAAAAA")
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        print("Meow")
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old, by the way, I am {self.color}")
    

class Dogg(Pet):
    def speak(self):
        print("Bark")

pet1 = Pet("Tim",19)
pet1.show()
pet1.speak()
pet2 = Cat("Bill", 44,"Blue")
pet2.show()
pet2.speak()


# - EXEMPLE 04 - - - - - - - - - - - - - - - - #
print('\n# - EXEMPLE 04 - - - - - - - - - - - - - - - - #\n')

class Person:
    number_of_people = 0

    def __init__(self,name):
        self.name = name
        Person.number_of_people += 1

print(Person.number_of_people)
p1 = Person("Xavier")
print(Person.number_of_people)
p2 = Person("Rosimary")


print(p1.number_of_people)

Person.number_of_people = 8
print(p2.number_of_people)

Person.number_of_people = 5
print(p1.number_of_people)