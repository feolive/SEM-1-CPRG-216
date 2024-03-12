'''Write an application that allows the user to choose a shape
from a menu, specify the shape’s dimension(s), and then
print the shape.'''

def main():
    print("Choose a shape from the following menu:")
    print("1. Line")
    print("2. Box")
    print("3. Triangle")
    print("4. Quit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        length = int(input("Enter the length of the line: "))
        line(length)
    elif choice == 2:
        width = int(input("Enter the width of the box: "))
        height = int(input("Enter the height of the box: "))
        box(width, height)
    elif choice == 3:
        height = int(input("Enter the height of the triangle: "))
        triangle(height)
    elif choice == 4:
        print("Goodbye!")
    else:
        print("Invalid choice")
    
def line(length):
    for i in range(length):
        print("*", end="")

def box(width, height):
    for i in range(height):
        print("*" * width)

def triangle(height):
    for i in range(height):
        print("*" * (i+1))

main()