# Create an empty dictionary
students = {}

# Read student details
while True:
    # Prompt for student details
    reg_num = input("Enter student's registration number: ")
    name = input("Enter student's name: ")

    # Add student details to dictionary
    students[reg_num] = name

    # Check if the user wants to enter more students
    more = input("Enter more students (y/n)? ")
    if more.lower() != "y":
        break

# Display the registration numbers
print("\nRegistration numbers:")
for reg_num in students.keys():
    print(reg_num)

# Display the names of students
print("\nNames of students:")
for name in students.values():
    print(name)
# Create an empty dictionary

