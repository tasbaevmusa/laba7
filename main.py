n = int(input("Enter size of dictionary: "))
rivers = {}
for i in range(n):
    country, river = input().split()
    rivers[river] = country

print("Enter name of river::")
search_rivers = input().split()
for river in search_rivers:
    if river in rivers:
        print(f"The river {river} flows in the country {rivers[river]}")
    else:
        print(f"The river {river} was not found in the dictionary")

new_river = input("Enter the name of the river you want to add: ")
if new_river in rivers:
    print(f"The river {new_river} already in the dictionary!")
else:
    new_country = input(f"Enter country, in which the river flows {new_river}: ")
    rivers[new_river] = new_country
    print(f"The river {new_river} added successfully!!!")

print("Update dictionary:")
for river, country in rivers.items():
    print(f"{country}: {river}")
