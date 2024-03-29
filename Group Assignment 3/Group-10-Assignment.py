import os
flag = None
menu_option = ""
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

def update_students(file_path, names, ids, gpas):
    f = open(file_path, "a")
    f.write(names[-1] + "," + ids[-1] + "," + str(gpas[-1]) + "\n")
    f.close()
 
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

def display_student_header():
    BORDER_DASH = "==========================================================================="
    print(BORDER_DASH)
    print("{:<25}{:^25}{:>25}".format("Student Name", "Student ID", "GPA"))
    print(BORDER_DASH)

def display_student(index, names, ids, gpas):
    display_student_header()
    print("{:<25}{:^25}{:>25}".format(names[index], ids[index], gpas[index]))

def list_students(names, ids, gpas):
    if len(names) > 0:
        display_student_header()
        for i in range(len(names)):
            print("{:<25}{:^25}{:>25}".format(names[i], ids[i], gpas[i]))
    else:
        print("Students list has no students")

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
        return names, ids, gpas, flag
    else:
        print(f"A student with ID {id} already exists.")
        flag = False
    
def main():
    file_path = input("Please enter the file name to load students information: ")
    while os.path.isfile(file_path) == True:
        menu()
        names = []
        ids = []
        gpas = []
        load_students(file_path, names, ids, gpas)
        if menu_option.upper() == 'L':
            list_students(names, ids, gpas)

        elif menu_option.upper() == 'A':
            add_students(names, ids, gpas)
            if flag == True:
                update_students(file_path, names, ids, gpas)
    else:
        print(file_path, "does not exist - Bye")
main()