from create_db import *

running = True

while running:
    selection = input('''Choose the option you would like to do:\n
    1. Create a Person
    2. Create a Course/Class
    3. Create a Cohort
    4. Assign a student to a Cohort
    5. Remove a tudent from a Cohort
    6. Deactivate a Course
    7. Deactivate a Person
    8. Deactivate a Cohort
    9. Complete a Course for a student
    10. Reactivate a Course
    11. Reactivate a Person
    12. Reactivate a Cohort
    13. Reactivate a student registered in a cohort
    14. View all active registrations for a cohort
    15. View all active cohorts for a course/class
    16. View all active people
    To quit the program, select "e" key and press enter\n
    Enter your selection: ''')
    if selection == "1":
        create_person()
        connection.commit()
    elif selection == "2":
        create_course()
        connection.commit()
    elif selection == "3":
        view_instructors()
        connection.commit()
    elif selection == "4":
        view_students()
        connection.commit()
    elif selection == "5":
        choose_cohort()
        connection.commit()
    elif selection == "6":
        view_active_courses()
        connection.commit()
    elif selection == "7":
        view_all_people()
        connection.commit()
    elif selection == "8":
        view_all_cohorts()
        connection.commit()
    elif selection == "9":
        view_all_cohorts_course_completion()
        connection.commit()
    elif selection == "10":
        reactivate_course()
        connection.commit()
    elif selection == "11":
        reactivate_person()
        connection.commit()
    elif selection == "12":
        reactivate_cohort()
        connection.commit()
    elif selection == "13":
        reactivate_student_cohort_registration()
        connection.commit()
    elif selection == "14":
        view_active_registrations()
        connection.commit()
    elif selection == "15":
        view_active_cohorts()
        connection.commit()
    elif selection == "16":
        view_active_people()
        connection.commit()
    elif selection == "e":
        running = False
    else:
        running = False
    choose_another = input("\nWould you like to select another option (y/n)? Enter:").lower()
    if choose_another == 'y':
        continue
    elif choose_another == 'n':
        running = False
