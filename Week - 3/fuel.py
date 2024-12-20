def main():
    fraction = get_int()
    convert_fraction(fraction)

def get_int():
    while True:
        try:
           return input("Fraction: ")
        except (ValueError, ZeroDivisionError):
            pass

def convert_fraction(n):
    x, y = n.split("/")

    result = (int(x)/int(y)) * 100

    if result < 1:
        print("E")
    elif result > 99:
        print("F")
    else:
        print(round(f"{result}%"))


main()