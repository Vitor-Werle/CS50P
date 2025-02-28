'''with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",") # rstrip remove os espaços e split retira a , 
        print(f"{row[0]} is in {row[1]}")'''

'''students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name" : name, "house": house}
        students.append(student)

def get_house(student): # conseguimos passar uma função para outra função
    return student["house"] # passamos a função sorted para a get_house

for student in sorted(students, key=get_house, reverse=True):
    print(f"{student['name']} is in {student['house']}")
  '''

students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name" : name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]): #lambda é equivalemnte a função get_name
    print(f"{student['name']} is in {student['house']}") # lambda seria uma função sem nome, ou seja, anônima
  