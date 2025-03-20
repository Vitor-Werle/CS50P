def main():
    dollars = dolars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like top tip? "))
    tip = dollars * percent
    print(f"leave ${tip:.2f}")

def dolars_to_float(d):
    # tirar os caracteres e deixar float
    dollar = d.replace("$", "")
    return float(dollar)

def percent_to_float(p):
    # tirar os caracteres, deixar float e dividir por 100
    percent = p.replace("%", "")
    return float(percent) / 100

main()