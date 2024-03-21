f = open("E:\SAIT\SEM-1-CPRG-216\Practice Labs\input.txt", "r")
fr = f.read()
c = 0
total = 0
lines = f.readlines()
for line in lines:
    line = line.split()
    total = total + int(line[2])
    c = c + 1
print("Total number of lines: ", c)
print("Total: ", total)