def menu():
    print("\nSimple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("0. Exit")
    while True:
        option = input("Enter menu option: ")
        if option.isdigit() and option in ['0', '1', '2', '3', '4']:
            return option

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return 'Cannot divide by 0'
    else:
        return x / y

def main():
    while True:
        option = menu()
        if option == '0':
            print("Calculator app closed")
            break
        else:
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))
            if option == '1':
                result = add(x, y)
                print(x, "+", y, "=", result)
            elif option == '2':
                result = subtract(x, y)
                print(x, "-", y, "=", result)
            elif option == '3':
                result = multiply(x, y)
                print(x, "*", y, "=", result)
            elif option == '4':
                result = divide(x, y)
                print(x, "/", y, "=", result)

if __name__ == "__main__":
    main()