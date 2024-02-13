#input a password
#check for at least 8 characters
#check for at least 1 number
#check for at least 1 uppercase letter
#check for at least 1 lowercase letter
#output valid or invalid message
valid = False
while not valid:
    password = input("Enter a password: ")
    if len(password) >=8:                                                                               
        digit_count = 0
        upper_count = 0
        lower_count = 0
        for char in password:
            if char.isdigit():
                digit_count += 1
            if char.isupper():
                upper_count += 1
            if char.islower():
                lower_count += 1
        if digit_count >= 1 and upper_count >= 1 and lower_count >= 1:
            valid = True      
    if valid:
        print("Passowrd is valid")
    else:
        print("Password is invalid, it should be at least 8 characters long, contain at least 1 number, 1 uppercase letter and 1 lowercase letter. Try again.")