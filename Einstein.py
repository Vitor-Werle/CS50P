def main():
    mass = int(input("m: "))
    print("E:", mass_to_joules(mass))

def mass_to_joules(m):
    return (m * 90000000000000000)

main()