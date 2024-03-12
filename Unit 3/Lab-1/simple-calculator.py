def main():
    i = 1
    while i>0:
        print("Simple Calculator")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("0. Exit")
        print("")

        #user input
        option = eval(input("Enter your menu option: "))
        if option == 0:
            print("Calculator app closed")
            break
        while True:
            try:
                option = int(input("Enter your menu option: "))
                if option in [1, 2, 3, 4]:
                    break
            except ValueError:
                option = eval(input("Enter your menu option: "))
                if option == 0:
                    print("Calculator app closed")
                    i = -1
        else:
            num_1 = float(input("Enter first number: "))
            num_2 = float(input("Enter second number: "))
            if option == 1:
                sum(num_1, num_2)
            elif option == 2:
                subtract(num_1, num_2)
            elif option == 3:
                multiply(num_1, num_2)
            elif option == 4:
                divide(num_1, num_2)

def sum(num_1, num_2):
    result = num_1 + num_2
    print(num_1, "+", num_2, "=", result)
    print("")

def subtract(num_1, num_2):
    result = num_1 - num_2
    print(num_1, "-", num_2, "=", result)
    print("")

def multiply(num_1, num_2):
    result = num_1 * num_2
    print(num_1, "*", num_2, "=", result)
    print("")

def divide(num_1, num_2):
    if num_2 == 0:
        print(num_1, "/", num_2,"=", "Cannot divide by zero")
        print("")
    else:
        result = num_1 / num_2
        print(num_1, "/", num_2, "=", result)
        print("")
main()