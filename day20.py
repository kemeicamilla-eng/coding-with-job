#SETS
#A set is a collection of unique elements

fruits = {"apple", "banana", "cherry", "date", "elderberry"}
print(fruits)

#creating sets
numbers = {1, 2, 3, 4, 5}
print(numbers)

numbers = set([9,8,7,6,5])
print(numbers)

names = ["John", "Jane", "Alice", "Bob", "John", "Alice"]

first_names = set(names)
print(first_names)

#Mistakes to avoid
my_set = {}  # This creates an empty dictionary, not a set{}
print(type(my_set))  # Output: <class 'dict'>

my_set = set()  # This creates an empty set
print(type(my_set))  # Output: <class 'set'>

numbers = {1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5}
print(numbers)  # Output: {1, 2, 3, 4, 5}

names =  {
    "John",
    "Jane",
    "Alice", 
    "Bob", 
}
print(names)  # Output: {'John', 'Jane', 'Alice', 'Bob'}

number = {10, 20, 30, 40, 50}
print(number) 


#Adding elements to a set
student = {"Naomi","Carol","Wanjiku"}
student.add("Peter")
print(student)  # Output: {'Naomi', 'Carol', 'Wanjiku', 'Peter'}

student.update(["Alice", "Bob"])
print(student)  # Output: {'Naomi', 'Carol', 'Wanjiku', 'Peter', 'Alice', 'Bob'}

student.remove("Carol")
print(student)  # Output: {'Naomi', 'Wanjiku', 'Peter', 'Alice', 'Bob'}

student.discard("Jane")
print(student)  # Output: {'Naomi', 'Wanjiku', 'Peter', 'Alice', 'Bob'}

students = student.pop()
print(students)  # Output: Randomly removes and returns an element from the set

cars = {"Toyota", "Honda", "Ford", "BMW"}
cars.clear()
print(cars)  # Output: set()

#Membership testing
Animals = {"Dog", "Cat", "Elephant", "Lion"}
print("Dog" in Animals)  # Output: True
print("Tiger" in Animals)  # Output: False
for animal in Animals:
    print(animal)  # Output: Dog, Cat, Elephant, Lion (order may vary)

python_students = {"Joy", "Faith","Job", "Mercy", "Esther"}
java_students = {"Luke", "Job", "Ann", "Bill"}

# Set operations
all_students = python_students.union(java_students)
print(all_students)

common_students = python_students & java_students 
print(common_students)

python_only = python_students - java_students
print(python_only)

result = python_students^(java_students)
print(result)  # Output: {'Joy', 'Faith', 'Ann', 'Bill', 'Mercy', 'Esther', 'Luke'}