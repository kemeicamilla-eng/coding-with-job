#Using functions with dictionaries
# We can use functions to manipulate dictionaries

student = {
    "John": 20,
    "Alice": 22,
    "Bob": 19
}

print(student)

#Accessing values in a dictionary using functions

def student(name, course):
    student = {
        "John": {"course": "Math", "score": 20},
        "Alice": {"course": "Physics", "score": 22},
        "Bob": {"course": "Chemistry", "score": 19}
    }

print(student("John", "Math"))  # Output: {'course': 'Math', 'score': 20}

#Accessing values in a dictionary using functions
def greet(name):
    return f"Hello, {name}!"

def farewell(name):
    return f"Goodbye, {name}!"

messages = {
    "hello": greet("John"),
    "goodbye": farewell("Alice")
}

print(messages)  # Output: {'hello': 'Hello, John!', 'goodbye': 'Goodbye, Alice!'}
