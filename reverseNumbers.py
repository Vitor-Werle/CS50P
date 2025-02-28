def main():
    numbers = get_numbers("Numbers: ")
    reserved_numbers = reverse_numbers(numbers)
    print(reserved_numbers)

def get_numbers(prompt):
    while True:
        try:
            numbers = int(input(prompt))
            if 100 <= numbers  <= 999:
                return numbers
            else:
                print("Coloque um número válido")
        except ValueError:
            pass

def reverse_numbers(n):
    return int(str(n)[::-1])


main()