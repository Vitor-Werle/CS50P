def main():
    phrase = input("Enter a word: ")
    print(remove_vowels(phrase))

def remove_vowels(phrase):
    result = ""
    lst = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

    for i in phrase:
        if i not in lst:
            result += i
        
    return result
    
if __name__ == "__main__":
    main()