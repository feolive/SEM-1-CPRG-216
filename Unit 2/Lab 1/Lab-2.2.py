#Sukhman Singh Lab - 2.2
#Write a program that computes both the circumference and the area of a circle for an entered radius.  Let the results be printed to the screen as specified below.  Variables should all be defined for circumference, area and radius in the program

#User Input
radius = float(input("Enter radius of circle (cm): ")) #radius of circle

pi = 3.1415926
#Calculations
circumference = 2 * pi * radius #circumference of circle
area = pi * radius ** 2 #area of circle

#Output
print("Circumference =", circumference, "cm")
print("Area =", area, "sqaure cm")