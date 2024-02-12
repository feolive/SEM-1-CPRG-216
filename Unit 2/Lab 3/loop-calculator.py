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
    option = int(input("Enter your menu option: "))
    if option == 0:
        print("Calculator app closed")
        i = 0
        
    else:
        num_1 = float(input("Enter first number: "))
        num_2 = float(input("Enter second number: "))

        #calculate the result
        if option == 1:
            result = num_1 + num_2
            print(num_1, "+", num_2, "=", result)
            print("")

        elif option == 2:
            result = num_1 - num_2
            print(num_1, "-", num_2, "=", result)
            print("")

        elif option == 3:
            result = num_1 * num_2
            print(num_1, "*", num_2, "=", result)
            print("")

        elif option == 4:
            if num_2 == 0:
                print("Cannot divide by zero")
                print("")
            else:
                result = num_1 / num_2
                print(num_1, "/", num_2, "=", result)
                print("")
    
