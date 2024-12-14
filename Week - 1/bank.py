def question(input):
    if "hello" in input:
        return "$0"
    elif "h" in input:
        return "$20"
    else: 
        return "$100"

answer = question(input("Greeting: "))
print(answer)

# pedir pro ChatGPT escrever isso em duas funções
