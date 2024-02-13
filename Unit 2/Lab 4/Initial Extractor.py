full_name = input("Enter your full name: ")

first_space = full_name.find(' ')
second_space = full_name.find(' ', first_space + 1)

first_initial = full_name[0].upper()
middle_initial = full_name[first_space + 1].upper()
last_initial = full_name[second_space + 1].upper()

print(first_initial + "." + middle_initial + "." + last_initial+".")
