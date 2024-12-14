def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    return (
        start_letters(s) and
        lenght_str(s) and
        have_number(s) and
        punctuation(s)
    )


def start_letters(s):
    return s[:2].isalpha()


def lenght_str(s):
    return 2 <= len(s) <= 6


def have_number(s):
    # Verifica se há números na string
    for i, char in enumerate(s):
        if char.isdigit():
            # Verifica se os números estão no final e se o primeiro número não é '0'
            return s[i:].isdigit() and s[i] != '0'
    return True


def punctuation(s):
    for i in s:
        if not i.isalnum():  # Verifica se não é letra nem número
            return False
    return True


main()
