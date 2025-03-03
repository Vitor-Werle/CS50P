'''with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",") # rstrip remove os espaços e split retira a , 
        print(f"{row[0]} is in {row[1]}")

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name" : name, "house": house}
        students.append(student)

def get_house(student): # conseguimos passar uma função para outra função
    return student["house"] # passamos a função sorted para a get_house

for student in sorted(students, key=get_house, reverse=True):
    print(f"{student['name']} is in {student['house']}")
  
import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row['name'], "home" : row['home']})


for student in sorted(students, key=lambda student: student["name"]): #lambda é equivalemnte a função get_name
    print(f"{student['name']} is in {student['home']}") # lambda seria uma função sem nome, ou seja, anônima
  '''

import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home "])
    writer.writerow({"name": name, "home": home})




    