class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}   # subject : grade

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

    def calculate_average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades.values()) / len(self.grades)


class GradeTracker:
    def __init__(self):
        self.students = []  # list of Student objects

    def add_student(self):
        name = input("Enter student name: ")
        student = Student(name)
        self.students.append(student)
        print(f"{name} added successfully!")

    def add_grades_to_student(self):
        name = input("Enter student name: ")
        student = self.find_student(name)

        if not student:
            print("Student not found!")
            return

        while True:
            subject = input("Enter subject (or 'done' to stop): ")
            if subject.lower() == "done":
                break
            grade = float(input(f"Enter grade for {subject}: "))
            student.add_grade(subject, grade)

        print(f"Grades added for {name}.")

    def find_student(self, name):
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None

    def show_average(self):
        name = input("Enter student name: ")
        student = self.find_student(name)

        if not student:
            print("Student not found!")
            return

        avg = student.calculate_average()
        print(f"{student.name}'s Average Grade is: {avg:.2f}")


# --------- MAIN PROGRAM ----------

tracker = GradeTracker()

while True:
    print("\n1. Add Student")
    print("2. Add Grades")
    print("3. Show Average")
    print("4. Exit")

    option = input("Choose an option: ")

    if option == "1":
        tracker.add_student()
    elif option == "2":
        tracker.add_grades_to_student()
    elif option == "3":
        tracker.show_average()
    elif option == "4":
        print("Program Finished.")
        break
    else:
        print("Invalid option!")
