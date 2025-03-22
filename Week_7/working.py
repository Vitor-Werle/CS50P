import re
import sys

def main():
    print(convert(input("Hours: ")))

def convert(s):  # Added parameter 's' which was missing
    isCorrectFormat = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)", s)
    if isCorrectFormat:
        pieces = isCorrectFormat.groups()
        if int(pieces[1]) > 12 or int(pieces[5]) > 12:
            raise ValueError
        first_time = new_format(pieces[1], pieces[2], pieces[3])
        second_time = new_format(pieces[5], pieces[6], pieces[7])
        return first_time + " to " + second_time
    else:
        raise ValueError

def new_format(hour, minute, am_pm):
    if am_pm == "PM":
        if int(hour) == 12:
            new_hour = 12
        else:
            new_hour = int(hour) + 12
    else:  # AM case
        if int(hour) == 12:
            new_hour = 0  # Fixed variable name from new_hours to new_hour
        else:
            new_hour = int(hour)
    
    if minute is None:  # Changed == to is for None comparison
        new_time = f"{new_hour:02d}:00"  # Added 'd' for decimal formatting
    else: 
        new_time = f"{new_hour:02d}:{minute}"  # Added 'd' for decimal formatting
    return new_time

if __name__ == "__main__":
    main()