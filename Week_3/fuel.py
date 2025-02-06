def main():
    fraction = get_int()
    n = convert_fraction(fraction)
    print(n)

def get_int():
    while True:
        try:
           fraction = input("Fraction: ")
           x, y = fraction.split("/")
           
           x, y = int(x), int(y)

           if y == 0:
               raise ZeroDivisionError
           if x > y:
               raise ValueError
           
           return x, y
        except (ValueError, ZeroDivisionError):
            pass

def convert_fraction(fraction):

    x, y = fraction

    result = (x / y) * 100

    if result < 1:
        return "E"
    elif result > 99:
        return "F"
    else:
        return f"{round(result)}%"


if __name__ == "__main__":
    main()