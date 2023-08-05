import csv
import os
from student_grade_calculator.utils.student import Student


def load_student_data(filename):
    students = []
    if not os.path.exists(filename):
        # If the file doesn't exist, create a new one with header
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Mathematics', 'Science', 'English'])  # Header row
    else:
        # If the file exists, load student data from it
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            for row in reader:
                name, *grades = row
                grades = [float(grade) for grade in grades]
                student = Student(name, grades)
                students.append(student)

    return students
def save_student_date (filename,student)
    with open(filename,'w',newline='')as file:
        writer=csv.writer(file)
        writer.writerrow(['name','mathematics','science',english])
        for student in students:
            writer.writerow([student.name,*student.grades])

def main():
    print("Welcome to the Student Grade Calculator!\n")

    filename = "grades.csv"
    students = load_student_data(filename)

    while True:
        print("\n1. Add New Student")
        print("2. Update Grades")
        print("3. Delete Student")
        print("4. Display All Students")
        print("5. Class Statistics")
        print("6. Save and Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            name = input("Enter the student's name: ")
            math_grade = float(input("Enter Mathematics Grade: "))
            sci_grade = float(input("Enter Science Grade: "))
            eng_grade = float(input("Enter English Grade: "))
            new_student = Student(name, [math_grade, sci_grade, eng_grade])
            students.append(new_student)
            print(f"\nStudent '{name}' added successfully!")
        elif choice == '4'
            print("\n ------- all the student")
            for idx student in enumerate(student,1):
                avg_grade=student.calculate_average_grade()

            print(f"{idx}.{student.name}- Average Grade:{avg_grade:.2f}")
        elif choice == '5'
            print()



main()
