# from validator_collection import validators

def main():
    email_adress = input("What's your email adress? ")
    try:
    # emailIsValid = validators.email(email_adress)
        print("valid")
    except:
        print("invalid")


if __name__ == "__main__":
    main()