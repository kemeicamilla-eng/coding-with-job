#python classes
# object oriented programming

# Class is a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object, with its properties and methods.
# phone
  #has a battery,ram,storage - attributes
  #can make calls, can send messages, can take photos - methods

# facebook
  #has a user base,posts,comments - attributes
  #can create posts, can comment on posts, can like posts - methods

# Camilla
#email = "camilla@example.com"
#name = "Camilla"

# Robert
#email = "robert@example.com"
#name = "Robert"

# Toyota
# wheels,doors,engine - design
#Class
#each car is an object of the class car

#class Student:
    #pass
#class  tells python that you are creating a new class.
#student is the name of the class. By convention, class names start with an uppercase letter.
#: starts the body of the class. The body of the class contains attributes and methods that define the behavior of the class.
#pass is a placeholder that indicates that the class has no attributes or methods defined yet. It is used to create an empty class.

#objects are instances of a class. An object is created by calling the class as if it were a function, passing any arguments that the class's __init__ method requires.
# student1 = Student()
#student1 creates a new student

#CONSTRUCTOR
#_init_()

#class Student:
    #def __init__(self, name, course):
        #self.name = name
        #self.course = course

#SELF
#self allows each object to keep it's own data.

#student1 = Student("Camilla", "Software Engineering")

#python thinks like
#self.name = "Camilla"
#self.course = "Software Engineering"

#Attributes are variables that belong to an object. They are used to store data that is associated with the object. In the Student class, name and course are attributes of the Student object.
#Accessing attributes
#print(self.name)

#METHODS
# functions inside a class

class Student:
    def __init__(self, name, course):
        self.name = name
        self.course = course

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am studying {self.course}.")

student1 = Student("Camilla", "Software Engineering")
student1.introduce()  # Output: Hello, my name is Camilla and I am studying Software Engineering.
student2 = Student("Robert", "Data Science")
student2.introduce()  # Output: Hello, my name is Robert and I am studying Data Science.
student3 = Student("Alice", "Cybersecurity")
student3.introduce()  # Output: Hello, my name is Alice and I am studying Cybersecurity.
student4 = Student("Bob", "Artificial Intelligence")
student4.introduce()  # Output: Hello, my name is Bob and I am studying Artificial Intelligence.
student5 = Student("Eve", "Machine Learning")
student5.introduce()  # Output: Hello, my name is Eve and I am studying Machine Learning.

