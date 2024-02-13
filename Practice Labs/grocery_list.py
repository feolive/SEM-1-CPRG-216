gorcery = []
item = input("Enter grocery item ('quit’ to quit):")
while item != "quit":
    gorcery.append(item)
    item = input("Next item: ")
print("Here is your grocery list:")
print(gorcery)