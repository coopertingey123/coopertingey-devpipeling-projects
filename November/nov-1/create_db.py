import sqlite3

connection = sqlite3.connect('database_schema.db')

cursor = connection.cursor()
# _____________________________________________________________________________________________
def create_registration(student_id, cohort_id):
    registration_date = "2021-11-02 00:00:00"
    values = student_id, cohort_id, registration_date
    print(values)
    cursor.execute("INSERT INTO Student_Cohort_Registration (student_id, cohort_id, registration_date) VALUES (?, ?, ?)", values)
    return

def view_cohort(student_id):
    cohorts = cursor.execute('''
    SELECT coh.cohort_id, name, first_name, last_name, start_date, end_date FROM Cohort coh
    JOIN People p
	    ON p.person_id = instructor_id
    JOIN Courses c
	    ON c.course_id = coh.course_id
    ''')
    print("Cohort ID   Course Name          Instructor Name      Start Date           End Date")
    for line in cohorts:
        print(f'{line[0]!s:<11} {line[1]:20} {line[2] + " " + line[3]:20} {line[4]:20} {line[5]:10}')
    cohort_select = int(input("Select the cohort you would like to join to the student. Enter: "))
    return create_registration(student_id, cohort_select)

def view_students():
    students = cursor.execute('''
    SELECT person_id, first_name, last_name  FROM People
    WHERE person_id NOT IN (Select instructor_id from Cohort)
    ''')
    print(f'Student ID     Student Name')
    for line in students:
        print(f'{line[0]:<14} {line[1]} {line[2]}')
    select_student = int(input("Choose a student ID to assign the student to a cohort. Enter: "))
    return view_cohort(select_student)

# view_students()

# _____________________________________________________________________________________

def create_cohort(course_id, instructor_id):
    start_date = input("Enter the start date for this course: ") #format this to fit the dates
    end_date = input("Enter an end date for this course: ") #format this to fit the dates
    values = instructor_id, course_id, start_date, end_date
    print(values)
    cursor.execute("INSERT INTO Cohort (instructor_id, course_id, start_date, end_date) VALUES (?, ?, ?, ?)", values)
    return

def view_courses(instructor_id):
    courses = cursor.execute(f"SELECT course_id, name, description FROM Courses JOIN People ON person_id = {instructor_id}")
    print(f'Course ID   Course Name          Course Description')
    for line in courses:
        print(f'{line[0]!s:<11} {line[1]!s:<20} {line[2]}')
    course_select = input("Select a course ID: ")
    return create_cohort(instructor_id, course_select)

def view_instructors():
    instructors = cursor.execute("SELECT person_id, first_name, last_name FROM People")
    print(f'Instructor ID        Instructor Name')
    print("--------------------------------------")
    for line in instructors:
        print(f'{line[0]!s:<20} {line[1]} {line[2]}')
    select_instructor = input("Choose an instructor ID to see what courses they offer. Enter: ")
    return view_courses(select_instructor)

# view_instructors()

# _____________________________________________________________________________________________
def create_person():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    email = input("Email: ")
    phone = input("Phone number: ")
    password = input("Password: ")
    address = input("Address: ")
    city = input("City: ")
    state = input("State: ")
    postal_code = input("Postal Code: ")
    list_of_values = first_name, last_name, email, phone, password, address, city, state, postal_code
    print(list_of_values)
    cursor.execute("INSERT INTO People (first_name, last_name, email, phone, password, address, city, state, postal_code) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", list_of_values)
    return

# create_person()
# _______________________________________________________________________________________
def create_course():
    name = input("Name of course: ")
    description = input("Course description: ")
    values = name, description
    print(values)
    cursor.execute("INSERT INTO Courses (name, description) VALUES (?, ?)", values)
    return

# create_course()

# __________________________________________________________________________________________
# Remove a Student from a Cohort
# A. This should just set the Student_Cohort_Registration record as active = 0 AND set the drop_date to today

# I want to see the students registered in any cohort
# The columns I want are: Student ID, Name of student, Cohort ID, Name of Course, Start date for cohort

def remove_student():
    return

def view_registered_students():
    students_in_cohort = cursor.execute('''
        SELECT student_id, first_name, last_name, cohort_id FROM Student_Cohort_Registration
        JOIN People
	        ON person_id = student_id
    ''')
    
    cohort_class_info = cursor.execute('''
        SELECT name, first_name, last_name, start_date, end_date FROM Cohort coh
        JOIN People p
            ON p.person_id = instructor_id
        JOIN Courses c
            ON c.course_id = coh.course_id
        WHERE cohort_id IN (SELECT cohort_id from Student_Cohort_Registration)
    ''')
    print("Cohort ID       Student ID          Name of Student          Course Name       Cohort Start Date      Cohort End Date")
    # for line in
    return



connection.commit()
