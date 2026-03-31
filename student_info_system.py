# Create an empty list to store all students
students = []

# Function to save students to a file
def save_to_file(student_list):
    with open("students.txt", "w") as file:
        for student in student_list:
            file.write(f"Name: {student['name']}\n")
            file.write(f"Student ID: {student['student_id']}\n")
            file.write(f"Favorite AI Tool: {student['favorite_AI_tool']}\n")
            file.write("---------------------------\n")

# Ask user for student details
name = input("Enter student name: ")
student_id = input("Enter student ID: ")
favorite_AI_tool = input("Enter favorite AI tool: ")

# Store data in a dictionary
student = {
    "name": name,
    "student_id": student_id,
    "favorite_AI_tool": favorite_AI_tool
}

# Append dictionary to list
students.append(student)

# Print number of students
print("\nTotal Students:", len(students))

# Print student details neatly
print("\nStudent Details")
print("---------------------------")
for s in students:
    print(f"Name: {s['name']}")
    print(f"Student ID: {s['student_id']}")
    print(f"Favorite AI Tool: {s['favorite_AI_tool']}")
    print("---------------------------")

# Save data to file
save_to_file(students)

print("Student data saved to students.txt")