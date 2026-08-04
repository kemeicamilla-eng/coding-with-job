#JSON
#JSON (JavaScript Object Notation) is a lightweight data interchange format that is easy for humans to read and write, and easy for machines to parse and generate.
{
"name": "John",
"age": 30,
"city": "New York"
}

#Converting a dictionary to JSON
import json
student = {
    "name": "Alice",
    "age": 20,
    "city": "London"
}
data = json.dumps(student)
print(data)  # Output: {"name": "Alice", "age": 20, "city": "London"}

#Converting JSON to a dictionary
import json
data = '{"name": "Alice", "age": 20, "city": "London"}'
student = json.loads(data)
print(student)  # Output: {'name': 'Alice', 'age': 20, 'city': 'London'}