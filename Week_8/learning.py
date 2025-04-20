class Dog:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner
    
    def bark(self):
        print("Auuuuuuuu")

class Owner():
    def __init__(self, name, age, contact):
        self.name = name
        self.age = age
        self.phone = contact

owner = Owner(input("Digite o nome do dono: "), int(input("Digite a idade do dono: ")), input("Digite o telefone do dono: "))
print(f"O dono é {owner.name}")
