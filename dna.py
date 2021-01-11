from cs50 import get_string
from sys import argv

if len(argv) != 3:
    print("Please read documents to follow the format of program")
    exit(0)

csv_file =open(argv[1],"r")

groups =[]
people= {}

for index,row in enumerate(csv_file):
    if index ==0:
        groups =[group for group in row.strip().split(",")][1:]
    else:
        current_row = row.strip().split(",")
        people[current_row[0]]= [int(y) for y in current_row[1:]]

dna_groups = open(argv[2], "r").read()

final_groups=[]

for group in groups:
    x=0
    current_max=0
    max_group =- 1

    while x < len(dna_groups):

        current_window = dna_groups[x:x + len(group)]

        if current_window == group:

            current_max+= 1

            max_group = max(max_group,current_max)

            x += len(group)
        else:
            current_max = 0
            x += 1

    final_groups.append(max_group)

for name,data in people.items():
    if data == final_groups:
        print(name)
        exit(1)

print("No match")





