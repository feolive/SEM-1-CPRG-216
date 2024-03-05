'''Define a tuple for territories holding these 3 items:  Northwest Territories, Yukon, Nunavut. Also define an empty dictionary.
For each entry in the tuple, read the population for that territory and then create a dictionary item using the territory name as the key and its population as the value.
Iterate through the dictionary you created, accumulating a population total and printing the report specified '''

BORDER = "=========================================="
TOTAL = 0
#territories tuple
territories = ('Northwest Territories', 'Yukon', 'Nunavut')

#dictionary to store population count
territory_population = {}

#adding population count to the dictionary
for territory in territories:
    population = int(input(f'Enter Population for {territory}: '))
    territory_population[territory] = population
#report
print("")
print(f"{'Terriotry': <30}\t{'Population': <30}")
print(BORDER)
for territory, population in territory_population.items():
    print(f"{territory: <30}\t{population: >10,d}")
    TOTAL += population
print(BORDER)
print(f"{'Total': <30}\t{TOTAL: >10,d}")