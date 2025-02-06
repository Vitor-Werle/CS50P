
def main():
    listing = get_int()
    ordenate_lst(listing)

def get_int(): #explicar toda essa parte 
    words = []
    verificar = set() # Assim que uma pessoa digita uma palavra, ela é armazenada em verificar, e se a pessoa digitar a mesma palavra novamente, ela não será armazenada novamente
    while True:
        try:
            lst = input("")
            if lst not in verificar: # I didn't understand
                words.append(lst) # I didn't understand
                verificar.add(lst) # I didn't understand
        except EOFError:
            break
    return words

def ordenate_lst(lst):
    for i, elem in enumerate(lst): # explicar melhor i elem e enumerate
        print(i + 1, ":", elem.upper())
    

    
main()

