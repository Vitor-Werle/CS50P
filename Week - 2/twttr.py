def main():
    phrase = input("Enter a word: ")
    remove_vowels(phrase)

def remove_vowels(phrase):
    result = ""
    lst = ['a', 'e', 'i', 'o', 'u']

    for i in phrase:
        if i not in lst:
            result += i
        
    print(result)
    
main()