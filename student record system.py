students = {}

#Adding students to the system
def add_student():
    name = input("Enter student name: ").title()

    if name in students:
        print("Student already exists!")
        return

    age = int(input("Enter student age: "))
    course = input("Enter student course: ")

    students[name] = {
        "age": age,
        "course": course
    }
    print(f"{name} has been added successfully!")


#searching for a student in the system
def search_student():
    name = input("Enter student name to search: ").title()

    if name in students:
        print("\nStudent found")
        print(f"Name: {name}")
        print(f"Age: {students[name]['age']}")
        print(f"Course: {students[name]['course']}")
    else:
        print("Student not found!")


#updating student information
def update_student():
    name = input("Enter student name to update: ").title()

    if name in students:
        print("\nStudent found")
        print(f"Name: {name}")
        print(f"Age: {students[name]['age']}")
        print(f"Course: {students[name]['course']}")

        age = int(input("Enter new age: "))
        course = input("Enter new course: ")

        students[name]['age'] = age
        students[name]['course'] = course

        print(f"{name}'s information has been updated successfully!")

    else:
        print("Student not found!")

#deleting a student from the system
def delete_student():
    name = input("Enter student name to delete: ").title()

    if name in students:
        del students[name]
        print(f"{name} has been deleted successfully!")
    else:
        print("Student not found!")


#displaying all students in the system
def display_students():
    if not students:
        print("No students found!")
        return

    print("\nAll Students:")
    for name, info in students.items():
        print(f"Name: {name}, Age: {info['age']}, Course: {info['course']}")

#main function to run the student record system
def main():
    while True:
        print("\nStudent Record System")
        print("1. Add Student")
        print("2. Search Student")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Display All Students")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_student()
        elif choice == '2':
            search_student()
        elif choice == '3':
            update_student()
        elif choice == '4':
            delete_student()
        elif choice == '5':
            display_students()
        elif choice == '6':
            print("Exiting the system...")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()