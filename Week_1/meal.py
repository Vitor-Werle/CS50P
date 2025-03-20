def main():
    time_convert = input("What time is it? ").replace(":",".")
    time_convert = float(time_convert)
    convert(time_convert)

def convert(time):
    if 7.00 <= time <= 8.00:
        print("breakfast time")
    elif 12.00 <= time <= 13.00:
        print("lunch time")
    elif 18.00 <= time <= 19.00:
        print("dinner time")
    else:
       return False

if __name__ == "__main__":
    main()
