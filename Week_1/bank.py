def main():
    question = (input("Greeting: ")).lower()
    print(value(question))

def value(greeting):
    if "hello" in greeting:
        return "$0"
    elif "h" in greeting:
        return "$20"
    else: 
        return "$100"
    
if __name__ == "__main__":
    main()