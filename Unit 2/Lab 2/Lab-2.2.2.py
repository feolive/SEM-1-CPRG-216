#Create a simple calculator that can add, subtract, multiply or divide depending upon the input from the user. 

print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

#user input
option = int(input("Enter your menu option: "))
num_1 = float(input("Enter first number: "))
num_2 = float(input("Enter second number: "))

#calculate the result
if option == 1:
    result = num_1 + num_2
    print(num_1, "+", num_2, "=", result)

elif option == 2:
    result = num_1 - num_2
    print(num_1, "-", num_2, "=", result)

elif option == 3:
    result = num_1 * num_2
    print(num_1, "*", num_2, "=", result)

elif option == 4:
    if num_2 == 0:
        print("Cannot divide by zero")
    else:
        result = num_1 / num_2
        print(num_1, "/", num_2, "=", result)
