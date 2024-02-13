yesterday = 0.7588
today = 0.7479
change = yesterday - today

#print output alingned to 2 columns
print(format("Date", ">10s"), format("Rate", ">10s"))
print(format("====", ">10s"), format("====", ">10s"))
print(format("Yesterday", ">10s"), format(yesterday, "+10.4f"))
print(format("Today", ">10s"), format(today, "+10.4f"))
print(format("Change", ">10s"), format(change, "+10.4f"))