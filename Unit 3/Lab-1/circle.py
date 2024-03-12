#import math module and rename it as PI
from math import pi as PI

# Main function to get the radius from the user and call the functions to calculate the circumference and area of the circle
def main():
    radius = eval(input("Give the radius of a circle: "))
    print("Circumference:", circumference(radius)," Area:", area(radius))

# Function to calculate the circumference of a circle
def circumference(radius):
    circumference = 2 * PI * radius
    circumference = format(circumference, ".3f")
    return circumference

# Function to calculate the area of a circle
def area(radius):
    area = PI * radius ** 2
    area = format(area, ".3f")
    return area

# Call the main function
main()