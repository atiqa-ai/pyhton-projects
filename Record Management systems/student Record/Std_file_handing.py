# This is a simple Python program for handling student records using file handling.
# It allows you to add new student records to a file and view all existing records.

def add_student():
    
    student_id = input("Enter student ID: ")
    
    # Ask for the student's name.
    student_name = input("Enter student name: ")
    
    # Ask for the student's marks (as a numeric value like 85.5).
    while True:
        try:
            student_marks = float(input("Enter student marks: "))
            break
        except ValueError:
            print("Invalid input! Please enter  int or float marks .")
    
    # If the file doesn't exist, it will be created.
    with open("students.txt", "a") as file:
        # Write the student record as a line in the file: ID,Name,Marks followed by a newline.
        file.write(f"{student_id},{student_name},{student_marks}\n")
    
    # Inform the user that the record was added.
    print("Student record added successfully!")

def view_students():
    
    # Try to open the file in "read" mode.
    try:
        with open("students.txt", "r") as file:
            # Read all lines from the file.
            lines = file.readlines()
            
            # Check if there are any records.
            if not lines:
                print("No student records found.")
                return
            
            # Print a header for clarity.
            print("Student Records:")
            print("ID\tName\t\tMarks")
            print("-" * 30)
            
            # Loop through each line and display the record.
            for line in lines:
                # Remove any trailing newline and split by comma to get ID, Name, Marks.
                parts = line.strip().split(",")
                if len(parts) == 3:  # Ensure the line has exactly 3 parts.
                    student_id, student_name, student_marks = parts
                    # Print in a formatted way (using tabs for alignment).
                    print(f"{student_id}\t{student_name}\t\t{student_marks}")
                else:
                    # If the line is malformed, skip it and print a warning.
                    print(f"Skipping invalid record: {line.strip()}")
    
    # If the file doesn't exist, inform the user.
    except FileNotFoundError:
        print("No student records file found. ")

# Now, the main part of the program: a loop that shows a menu and handles user choices.
def main():
    
    # Start an infinite
    while True:
        print("\nStudent Record Management")
        print("1. Add Student Record")
        print("2. View Student Records")
        print("3. Exit")
        
        choice = input("Enter your choice (1-3): ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 3.")
if __name__ == "__main__":
    main()  