# Student Grade Management System

students = []   # list to store all student records

# Function to calculate grade
def calculate_grade(avg):
    if avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Fail"


# Function to add a student
def add_student():
    try:
        name = input("Enter student name: ")
        if name.isdigit():
            raise ValueError("Name cannot be numeric")

        marks1 = int(input("Enter marks for Subject 1: "))
        marks2 = int(input("Enter marks for Subject 2: "))
        marks3 = int(input("Enter marks for Subject 3: "))

        if marks1 < 0 or marks2 < 0 or marks3 < 0:
            raise ValueError("Marks cannot be negative")

        total = marks1 + marks2 + marks3
        average = total / 3
        grade = calculate_grade(average)

        student = {
            "Name": name,
            "Total": total,
            "Average": average,
            "Grade": grade
        }

        students.append(student)
        print("✅ Student added successfully!")

    except ValueError as e:
        print("❌ Error:", e)


# Function to display all students
def display_students():
    if not students:
        print("❌ No student records found.")
        return

    # Showing list is inside (raw data)
    print("Students List (Raw Data):")
    print(students)

    print("--- Student Results ---")
    for i, s in enumerate(students, start=1):
        print(f"Student {i}")
        print("Name:", s["Name"])
        print("Total:", s["Total"])
        print("Average:", round(s["Average"], 2))
        print("Grade:", s["Grade"])
        print("-----------------------")


# Main program loop
while True:
    print("Student Grade Management System")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        print("Thank you! Exiting program 👋")
        break
    else:
        print("❌ Invalid choice! Try again.")
