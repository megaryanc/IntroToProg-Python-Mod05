# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script
#   <Ryan Choi>,<11/16/2024>, <Advanced Collections and Error Handling>
# ------------------------------------------------------------------------------------------ #
import json

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
# Define the Data Constants
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
student_data: dict[str,str] = {} # one row of student data
students: list = []  # a table of student data
json_data: str = ''  # a text-based format for storing and exchanging data that is both human-readable and machine-parsable.
file = None  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file
try:
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
except FileNotFoundError: # if file does not exist.
    print('File not found. Starting with empty list.') # notifies user of file not found.
except Exception as e: #for any other errors.
    print(f'Error code: {e}')

    
# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input user data
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name: # if left empty
                raise ValueError('First name missing.')
            student_last_name = input("Enter the student's last name: ")
            if not student_last_name: # if left empty
                raise ValueError('Last name missing.')
            course_name = input("Please enter the name of the course: ")
            student_data = {
                            'FirstName': student_first_name,     # rename for easier recall.
                            'LastName': student_last_name,
                            'CourseName': course_name
            }
            students.append(student_data)
            print(f"You have registered {student_first_name} {student_last_name} for {course_name}.")
        except ValueError as ve:
            print(f'Error code: {ve}')
        except Exception as e:
            print(f'Error code: {e}')
        continue

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print(f"Student {student['FirstName']} {student['LastName']} is enrolled in {student['CourseName']}")
        print("-"*50)
        continue
    # Save the data to a file
    elif menu_choice == "3":
        try:
            with open(FILE_NAME, "w") as file:
                json.dump(students, file)
            file.close()
        except ValueError as ve:
            print(f'Error code: {ve}')
        except Exception as e:
            print(f'Error code: {e}')
        file.close()
        print("The following data was saved to file!")
        continue

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, or 3")
print("Program Ended")
