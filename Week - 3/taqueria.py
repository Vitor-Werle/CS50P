menu = {
    "baja taco": 4.25,
    "burrito": 7.50,
    "bowl": 8.50,
    "nachos": 11.00,
    "quesadilla": 8.50,
    "super burrito": 8.50,
    "super quesadilla": 9.50,
    "taco": 3.00,
    "tortilla salad": 8.00
}

total = 0
while True:
    try:
        item = input("item: ").lower() 
        if item in menu:
            total += menu[item]
            print(total)
        else: 
            pass
    except EOFError:
        break



# Recebe o nome (se for diferenta do lista, pedir de novo) e printar o valor
# Se digitar mais nome, printe o valor total (do item anterior e desse)
# Sai do loop quando usar o control-d
# Se digitar o item errado pede para digitar de novo