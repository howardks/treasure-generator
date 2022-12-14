import random

name_list = list()
adj_list = list()

with open("nameList.txt") as names :
    for x in names :
        name_list.append(names.readline().strip()) 

with open("adjectiveList.txt") as adjs :
    for x in adjs:
        adj_list.append(adjs.readline().strip())

user_num = input("How many items: ")
print("\nTreasure: ")

for x in range(int(user_num)) :
    value = str(random.randint(0, 1)) + "gp " + str(random.randint(0, 5)) + "sp " + str(random.randint(0, 9)) + "cp"
    print(random.choice(adj_list) + " " + random.choice(name_list) + "\t\tValue: " + value)