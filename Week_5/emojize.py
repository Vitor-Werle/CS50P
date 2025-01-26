import emoji

def main():
    argument = input("Input: ")
    print(emojize(argument))

def emojize(n):
    return emoji.emojize(n)

main()