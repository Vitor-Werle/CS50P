def main():
    with open("alice.txt", "r") as file:
        contents = file.readlines()

    charpter1 = contents[17:242]

    with open("newfile.txt", "w") as file:
        file.writelines(charpter1)


main()