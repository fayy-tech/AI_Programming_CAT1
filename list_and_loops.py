# Create a list of student names
students = ["Monicah", "Irwine", "Benedict", "Gloria", "Faith", "Teddy", "Sandra", "Drina", "Ryan"]

# Loop through the list and print each name with its index
for i in range(len(students)):
    print(f"{i+1}. {students[i].upper()}")