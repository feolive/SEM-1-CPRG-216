#Write a program that reads in temperatures and puts them in a list.  
#Stop inputting when a temperature of 999 is entered.
#Calculate the average temperature.  
#Iterate through the list you created and count how many of the temperatures are above average.  
#Print out the results as specified in the sample run below.

#emply list
temp = []
#sum of the temperatures
sum = 0
#input temperature
in_temp = eval(input("Enter a temperature: "))
#while input is not 999
while in_temp != 999:
    temp.append(in_temp)
    sum += in_temp
    in_temp = eval(input("Enter a temperature: "))
#calculate the average
average = sum / len(temp)
print("The average temperature is", average)