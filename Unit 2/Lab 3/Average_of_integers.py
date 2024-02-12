#user input
value = int(input("Enter an integer > 1: "))

#intial value
sum = 0

#for loop
for i in range(1, value + 1):
    sum += i
print("")
print("The average of the integers 1...", value,"is ", sum / value)