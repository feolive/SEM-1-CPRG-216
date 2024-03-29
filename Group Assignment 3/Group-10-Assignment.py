#Importing the os module
import os

#Declaring the global variables
flag = None
menu_option = ""
index = 0

#Function to load the students information from the file
def load_students(file_path, names, ids, gpas):
    f = open(file_path, "r")
    lines = f.readlines()
    for line in lines:
        student = line.split(",")
        names.append(student[0])
        ids.append(student[1])
        gpas.append(float(student[2]))
    f.close()
    return names, ids, gpas

#Function to update the students information in the file
def update_students(file_path, names, ids, gpas):
    f = open(file_path, "w")
    for i in range(len(names)):
        f.write(names[i] + "," + ids[i] + "," + str(gpas[i]) + "\n")
    f.close()

#Function to display the menu
def menu():
    BORDER_STAR = "*"*75
    print(BORDER_STAR)
    print("{:^{}}".format("*** Student Registration System ***", len(BORDER_STAR)))
    print(BORDER_STAR)
    print("Select from the following options")
    print("L - List Students")
    print("A - Add Student")
    print("E - Edit Student")
    print("D - Delete Student")
    print("F - Find A Student")
    print("G - GPA Average")
    print("Q - Quit")
    while True:
        global menu_option
        menu_option = input()
        if menu_option.upper() in ['L', 'A', 'E', 'D', 'F', 'G', 'Q']:
            return menu_option
        else:
            print("Invalid Input")

#Function to display the student header
def display_student_header():
    BORDER_DASH = "="*75
    print(BORDER_DASH)
    print("{:<25}{:^25}{:>25}".format("Student Name", "Student ID", "GPA"))
    print(BORDER_DASH)

#Function to display the student
def display_student(index, names, ids, gpas):
    print("{:<25}{:^25}{:>25}".format(names[index], ids[index], gpas[index]))

#Function to list the students
def list_students(names, ids, gpas):
    if len(names) > 0:
        display_student_header()
        for i in range(len(names)):
            print("{:<25}{:^25}{:>25}".format(names[i], ids[i], gpas[i]))
    else:
        print("Students list has no students")

#Function to add the students
def add_students(names, ids, gpas):
    global flag
    flag = False
    id = input("Enter the student ID: ")
    if id not in ids:
        name = input("Enter the student name: ")
        gpa = float(input("Enter the student GPA: "))
        names.append(name)
        ids.append(id)
        gpas.append(gpa)
        flag = True
        print(f"A student with ID {id} is added.")
        return names, ids, gpas, flag
    else:
        print(f"A student with ID {id} already exists.")
        flag = False

#Function to edit the students
def edit_student(index, names, ids, gpas):
    names[index] = input("Enter the new student name to edit: ")
    ids[index] = input("Enter the new student ID to edit: ")
    gpas[index] = float(input("Enter the new student GPA to edit: "))
    return names, ids, gpas

#Function to delete the students
def delete_student(index, names, ids, gpas):
    names = names.pop(index)
    ids = ids.pop(index)
    gpas = gpas.pop(index)
    print(f"Student with ID {ids} is deleted.")
    return names, ids, gpas

def find_student(id, ids):
    if id in ids:
        global index
        global flag
        index = ids.index(id)
        flag = True
        return index, flag
    else:
        print(f"No student with ID {id}")
        flag = False

#Function to calculate the average GPA
def calculate_gpa_average(gpas):
    print("GPA Average is ", format(sum(gpas)/len(gpas), ".2f"))
    
#main function
def main():
    file_path = input("Please enter the file name to load students information: ")
    if os.path.isfile(file_path) == True:
        print("Students information has been loaded from the file")
    while os.path.isfile(file_path) == True:
        menu()
        names = []
        ids = []
        gpas = []
        load_students(file_path, names, ids, gpas)

        #When the user selects the option to list the students
        if menu_option.upper() == 'L':
            list_students(names, ids, gpas)

        #When the user selects the option to add the students
        elif menu_option.upper() == 'A':
            print("Adding a student .....")
            add_students(names, ids, gpas)
            if flag == True:
                update_students(file_path, names, ids, gpas)

        #When the user selects the option to edit the students
        elif menu_option.upper() == 'E':
            id_check = input("Enter the student ID to edit: ")
            if id_check in ids:
                global index
                index = ids.index(id_check)
                edit_student(index, names, ids, gpas)
                update_students(file_path, names, ids, gpas)
            else:
                print(f"A student with ID {id_check} does not exist.")

        #When the user selects the option to delete the students
        elif menu_option.upper() == 'D':
            option_delete = input("Enter the student ID to delete: ")
            if option_delete in ids:
                index = ids.index(option_delete)
                delete_student(index, names, ids, gpas)
                update_students(file_path, names, ids, gpas)
            else:
                print(f"No student with ID {option_delete}")
        
        #When the user selects the option to find the students
        elif menu_option.upper() == 'F':
            id = input("Enter student id: ")
            find_student(id, ids)
            if flag == True:
                display_student_header()
                display_student(index, names, ids, gpas)
        
        #When the user selects the option to calculate the average GPA
        elif menu_option.upper() == 'G':
            calculate_gpa_average(gpas)
        
        #When the user selects the option to quit
        elif menu_option.upper() == 'Q':
            print("Thanks and Good Bye")
            print("Please press enter to continue....")
            break
    else:
        print(file_path, "does not exist - Bye")
main()