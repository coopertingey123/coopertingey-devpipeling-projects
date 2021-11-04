import sqlite3

connection = sqlite3.connect('database_schema.db')

cursor = connection.cursor()
# _____________________________________________________________________________________________
# Register a student for a cohort

def register_student():
    students = cursor.execute('''
    SELECT person_id, first_name, last_name  FROM People
    WHERE person_id NOT IN (Select instructor_id from Cohort)
    AND active = 1
    ''')
    print(f'\nStudent ID     Student Name')
    for line in students:
        print(f'{line[0]:<14} {line[1]} {line[2]}')
    select_student = int(input("\nChoose a student ID to assign the student to a cohort. Enter: "))
    cohorts = cursor.execute('''
    SELECT coh.cohort_id, name, first_name, last_name, start_date, end_date FROM Cohort coh
    JOIN People p
	    ON p.person_id = instructor_id
    JOIN Courses c
	    ON c.course_id = coh.course_id
    WHERE coh.active = 1
    ''')
    print("\nCohort ID   Course Name          Instructor Name      Start Date           End Date")
    for line in cohorts:
        print(f'{line[0]!s:<11} {line[1]:20} {line[2] + " " + line[3]:20} {line[4]:20} {line[5]:10}')
    cohort_select = int(input("\nSelect the cohort you would like to join to the student. Enter: "))
    registration_date = "2021-11-02 00:00:00"
    values = select_student, cohort_select, registration_date
    cursor.execute("INSERT INTO Student_Cohort_Registration (student_id, cohort_id, registration_date) VALUES (?, ?, ?)", values)
    return

# register_student()

# _____________________________________________________________________________________
# Create a cohort

def create_cohort():
    instructors = cursor.execute("SELECT person_id, first_name, last_name FROM People WHERE active = 1")
    print(f'\nInstructor ID        Instructor Name')
    for line in instructors:
        print(f'{line[0]!s:<20} {line[1]} {line[2]}')
    select_instructor = int(input("\nChoose an instructor ID to assign them to a course. Enter: "))
    courses = cursor.execute(f"SELECT course_id, name, description FROM Courses JOIN People ON person_id = ? WHERE active = 1", (select_instructor,))
    print(f'\nCourse ID   Course Name          Course Description')
    for line in courses:
        print(f'{line[0]!s:<11} {line[1]!s:<20} {line[2]}')
    course_select = int(input("\nSelect a course ID to assign the instructor to the course. Enter: "))
    start_date = input("Enter the start date for this course: ") #format this to fit the dates
    end_date = input("Enter an end date for this course: ") #format this to fit the dates
    values = select_instructor, course_select, start_date, end_date
    cursor.execute("INSERT INTO Cohort (instructor_id, course_id, start_date, end_date) VALUES (?, ?, ?, ?)", values)
    print("The cohort has been added.")
    return

# view_instructors()

# _____________________________________________________________________________________________
# Create a person

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
    cursor.execute("INSERT INTO People (first_name, last_name, email, phone, password, address, city, state, postal_code) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", list_of_values)
    return

# create_person()
# _______________________________________________________________________________________
# Create a course

def create_course():
    name = input("Name of course: ")
    description = input("Course description: ")
    values = name, description
    cursor.execute("INSERT INTO Courses (name, description) VALUES (?, ?)", values)
    return

# create_course()

# __________________________________________________________________________________________
# Remove a student from a cohort

def remove_student():
    cohorts = cursor.execute('''
    SELECT coh.cohort_id, name, first_name, last_name, start_date, end_date FROM Cohort coh
    JOIN People p
	    ON p.person_id = instructor_id
    JOIN Courses c
	    ON c.course_id = coh.course_id
    WHERE coh.active = 1
    ''')
    print("\nCohort ID   Course Name          Instructor Name      Start Date           End Date")
    for line in cohorts:
        print(f'{line[0]!s:<11} {line[1]:20} {line[2] + " " + line[3]:20} {line[4]:20} {line[5]:10}')
    cohort_select = int(input("\nChoose a cohort ID to see the students registered. Enter: "))
    students_in_cohort = cursor.execute('''
        SELECT scr.student_id, first_name, last_name, scr.registration_date, scr.completion_date FROM Student_Cohort_Registration scr
        JOIN People 
	        ON person_id = scr.student_id
        WHERE scr.cohort_id = ?
	    AND scr.active = 1
    ''', (cohort_select,))
    print("\nStudent ID   Student Name    Registration Date      Completion Date")
    for line in students_in_cohort:
        if line[4]:
            print(f'{line[0]!s:<11} {line[1] + " " + line[2]:15} {line[3]:20} {line[4]:20}')
        else:
            print(f'{line[0]!s:<11} {line[1] + " " + line[2]:15} {line[3]:20}')
    select_student_id = input("\nSelect the student you would like to remove from the cohort. Enter: ")
    values = select_student_id, cohort_select
    cursor.execute('''
        UPDATE Student_Cohort_Registration
        SET active = 0, drop_date = "todays date"
        WHERE student_id = ?
        AND cohort_id = ?
    ''', values)
    print("\nStudent has been removed from Cohort.")
    return

# remove_student()

# ________________________________________________________________________________________
# Deactivate a Course

def deactivate_course():
    courses = cursor.execute('''
        SELECT course_id, name, description FROM Courses
        WHERE active = 1
    ''')
    print("\nCourse ID    Course Name            Description")
    for line in courses:
        print(f'{line[0]:<12} {line[1]:<22} {line[2]}')
    select_course = int(input("\nSelect the course you would like to deactivate. Enter: "))
    cursor.execute('''
        UPDATE Courses
        SET active = 0
        WHERE course_id = ?
    ''', (select_course,))
    print("\nThe course has been deactivated. Now it cannot be used to create a cohort.")
    return

# deactivate_course()

# ____________________________________________________________________________________
# Deactivate a Person (They can no longer be selected for new Registrations or as an instructor for a Cohort)

def deactivate_person():
    people = cursor.execute('''
    SELECT person_id, first_name, last_name, email FROM People
    WHERE active = 1
    ''')
    print("\nPerson ID     Name                Email")
    for line in people:
        print(f'{line[0]:<13} {line[1] + " " + line[2]:19} {line[3]}')
    person_select = int(input("\nSelect the ID of the person you would like to deactivate. Enter: "))
    cursor.execute('''
    UPDATE People
    SET active = 0
    WHERE person_id = ?
    ''', (person_select,))
    print("\nThis person has been deactivated. They no longer can be selected for new Registrations or as an instructor for a Cohort.")
    return

# deactivate_person()
# _____________________________________________________________________________________________
# Deactivate a Cohort (They can no longer be selected for new student registrations)

def deactivate_cohort():
    cohorts = cursor.execute('''
        SELECT coh.cohort_id, name, first_name, last_name, start_date, end_date FROM Cohort coh
        JOIN People p
            ON p.person_id = instructor_id
        JOIN Courses c
            ON c.course_id = coh.course_id
        WHERE coh.active = 1
    ''')
    print("\nCohort ID   Course Name          Instructor Name      Start Date           End Date")
    for line in cohorts:
        print(f'{line[0]!s:<11} {line[1]:20} {line[2] + " " + line[3]:20} {line[4]:20} {line[5]:10}')
    cohort_select = int(input("\nChoose a cohort ID to deactivate the Cohort. Enter: "))
    cursor.execute('''
        UPDATE Cohort
        SET active = 0
        WHERE cohort_id = ?
    ''', (cohort_select,))
    print("This Cohort has been deactivated. It can no longer be selected for new student registrations.")
    return

# deactivate_cohort()
# _________________________________________________________________________________
# Complete a Course for a Student. This will set the completion date on the Student_Cohort_Registration.

def view_all_cohorts_course_completion():
    cohorts = cursor.execute('''
        SELECT coh.cohort_id, name, first_name, last_name, start_date, end_date FROM Cohort coh
        JOIN People p
            ON p.person_id = instructor_id
        JOIN Courses c
            ON c.course_id = coh.course_id
        WHERE coh.active = 1
    ''')
    print("\nCohort ID   Course Name          Instructor Name      Start Date           End Date")
    for line in cohorts:
        print(f'{line[0]!s:<11} {line[1]:20} {line[2] + " " + line[3]:20} {line[4]:20} {line[5]:10}')
    cohort_select = int(input("\nChoose a cohort ID to see the students registered. Enter: "))
    students_in_cohort = cursor.execute('''
        SELECT scr.student_id, first_name, last_name, scr.registration_date, scr.completion_date FROM Student_Cohort_Registration scr
        JOIN People 
	        ON person_id = scr.student_id
        WHERE scr.cohort_id = ?
	    AND scr.active = 1
    ''', (cohort_select,))
    print("\nStudent ID   Student Name    Registration Date      Completion Date")
    for line in students_in_cohort:
        if line[4]:
            print(f'{line[0]!s:<11} {line[1] + " " + line[2]:15} {line[3]:20} {line[4]:20}')
        else:
            print(f'{line[0]!s:<11} {line[1] + " " + line[2]:15} {line[3]:20}')
    select_student_id = input("\nSelect the student you would like to remove from the cohort. Enter: ")
    values = select_student_id, cohort_select
    # Make sure and format the date here
    cursor.execute('''
        UPDATE Student_Cohort_Registration
        SET active = 0, completion_date = "todays date" 
        WHERE student_id = ?
        AND cohort_id = ?
    ''', values)
    print("\nStudent has been deactivated and given a completion date for this Cohort.")
    return

# _______________________________________________________________________________________________
# Reactivate Course, Person, Cohort, Student_Cohort_Registration
def reactivate_course():
    inactive_courses = cursor.execute('''
        SELECT course_id, name, description FROM Courses
        WHERE active = 0
    ''')
    print("\nCourse ID    Course Name            Description")
    for line in inactive_courses:
        print(f'{line[0]:<12} {line[1]:<22} {line[2]}')
    select_course = int(input("\nSelect the course you would like to reactivate. Enter: "))
    cursor.execute('''
        UPDATE Courses
        SET active = 1
        WHERE course_id = ?
    ''', (select_course,))
    print("\nThe course is now active. It can again be used to create a cohort.")
    return
# reactivate_course()

def reactivate_person():
    inactive_people = cursor.execute('''
        SELECT person_id, first_name, last_name, email FROM People
        WHERE active = 0
    ''')
    print("\nPerson ID     Name                Email")
    for line in inactive_people:
        print(f'{line[0]:<13} {line[1] + " " + line[2]:19} {line[3]}')
    person_select = int(input("\nSelect the ID of the person you would like to reactivate. Enter: "))
    cursor.execute('''
        UPDATE People
        SET active = 1
        WHERE person_id = ?
    ''', (person_select,))
    print("\nThe person is now active and can be used as a student or instructor.")
    return
# reactivate_person()

def reactivate_cohort():
    inactive_cohorts = cursor.execute('''
        SELECT coh.cohort_id, name, first_name, last_name, start_date, end_date FROM Cohort coh
        JOIN People p
            ON p.person_id = instructor_id
        JOIN Courses c
            ON c.course_id = coh.course_id
        WHERE coh.active = 0
    ''')
    print("\nCohort ID   Course Name          Instructor Name      Start Date           End Date")
    for line in inactive_cohorts:
        print(f'{line[0]!s:<11} {line[1]:20} {line[2] + " " + line[3]:20} {line[4]:20} {line[5]:10}')
    cohort_select = int(input("\nChoose a cohort ID to reactivate the Cohort. Enter: "))
    cursor.execute('''
        UPDATE Cohort
        SET active = 1
        WHERE cohort_id = ?
    ''', (cohort_select,))
    print("This Cohort is now active. It can be selected again for new student registrations.")
    return
# reactivate_cohort()

def reactivate_student_cohort_registration():
    cohorts = cursor.execute('''
        SELECT coh.cohort_id, name, first_name, last_name, start_date, end_date FROM Cohort coh
        JOIN People p
            ON p.person_id = instructor_id
        JOIN Courses c
            ON c.course_id = coh.course_id
        WHERE coh.active = 1
    ''')
    print("\nCohort ID   Course Name          Instructor Name      Start Date           End Date")
    for line in cohorts:
        print(f'{line[0]!s:<11} {line[1]:20} {line[2] + " " + line[3]:20} {line[4]:20} {line[5]:10}')
    cohort_select = int(input("\nChoose a cohort ID to see the inactive students for the class. Enter: "))
    inactive_students_in_cohort = cursor.execute('''
        SELECT scr.student_id, first_name, last_name, scr.registration_date, scr.completion_date FROM Student_Cohort_Registration scr
        JOIN People 
	        ON person_id = scr.student_id
        WHERE scr.cohort_id = ?
	    AND scr.active = 0
    ''', (cohort_select,))
    print("\nStudent ID   Student Name    Registration Date      Completion Date")
    for line in inactive_students_in_cohort:
        if line[4]:
            print(f'{line[0]!s:<11} {line[1] + " " + line[2]:15} {line[3]:20} {line[4]:20}')
        else:
            print(f'{line[0]!s:<11} {line[1] + " " + line[2]:15} {line[3]:20}')
    select_student_id = input("\nSelect the student you would like to reactivate to the cohort. Enter: ")
    cursor.execute('''
        UPDATE Student_Cohort_Registration
        SET active = 1
        WHERE student_id = ?
        AND cohort_id = ?
    ''', (select_student_id, cohort_select))
    print("\nStudent has been reactivated and kept the same completion date for this Cohort.")
    return
# reactivate_student_cohort_registration()

# _________________________________________________________________________________________________
# View active registrations for a cohort

def view_active_registrations():
    cohorts = cursor.execute('''
        SELECT coh.cohort_id, name, first_name, last_name, start_date, end_date FROM Cohort coh
        JOIN People p
            ON p.person_id = instructor_id
        JOIN Courses c
            ON c.course_id = coh.course_id
        WHERE coh.active = 1
    ''')
    print("\nCohort ID   Course Name          Instructor Name      Start Date           End Date")
    for line in cohorts:
        print(f'{line[0]!s:<11} {line[1]:20} {line[2] + " " + line[3]:20} {line[4]:20} {line[5]:10}')
    select_cohort = int(input("Select a cohort to see active students in the cohort. Enter: "))
    students_in_cohort = cursor.execute('''
        SELECT scr.student_id, first_name, last_name, scr.registration_date, scr.completion_date FROM Student_Cohort_Registration scr
        JOIN People 
	        ON person_id = scr.student_id
        WHERE scr.cohort_id = ?
	    AND scr.active = 1
    ''', (select_cohort,))
    print("\nStudent ID   Student Name    Registration Date      Completion Date")
    for line in students_in_cohort:
        if line[4]:
            print(f'{line[0]!s:<11} {line[1] + " " + line[2]:15} {line[3]:20} {line[4]:20}')
        else:
            print(f'{line[0]!s:<11} {line[1] + " " + line[2]:15} {line[3]:20}')
    return

# view_active_registrations()

# _____________________________________________________________________________________________________
# view active cohorts for a course

def view_active_cohorts():
    cohorts = cursor.execute('''
        SELECT coh.cohort_id, name, first_name, last_name, start_date, end_date FROM Cohort coh
        JOIN People p
            ON p.person_id = instructor_id
        JOIN Courses c
            ON c.course_id = coh.course_id
        WHERE coh.active = 1
    ''')
    print("\nCohort ID   Course Name          Instructor Name      Start Date           End Date")
    for line in cohorts:
        print(f'{line[0]!s:<11} {line[1]:20} {line[2] + " " + line[3]:20} {line[4]:20} {line[5]:10}')
    return

# view_active_cohorts()
# ______________________________________________________________________________________________--
# view all active people

def view_active_people():
    people = cursor.execute('''
        SELECT person_id, first_name, last_name, email FROM People
        WHERE active = 1
    ''')
    print("\nPerson ID     Name                Email")
    for line in people:
        print(f'{line[0]:<13} {line[1] + " " + line[2]:19} {line[3]}')
    return
# view_active_people()

connection.commit()
