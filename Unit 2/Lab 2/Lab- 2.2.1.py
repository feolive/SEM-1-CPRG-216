#Write a program that asks the user to enter a GIC term in years and an amount to invest.
term = int(input("Enter GIC Term: "))
if term > 5:
    print("The term must be 5 years or less")
amount = float(input("Enter the amount to invest: "))

#interest rates in percentage
INT_1 = 4.9
INT_2 = 4.1
INT_3 = 4.0
INT_4 = 3.8
INT_5 = 3.75

#calculate the interest
if term == 1:
    interest = amount * (INT_1 / 100) * term
elif term == 2:
    interest = amount * (INT_2 / 100) * term
elif term == 3:
    interest = amount * (INT_3 / 100) * term
elif term == 4:
    interest = amount * (INT_4 / 100) * term
elif term == 5:
    interest = amount * (INT_5 / 100) * term
total = interest + amount

print("Interest at end of term = $", format(interest, ",.2f"))
print("Total at end of term = $", format(total, ",.2f"))
    