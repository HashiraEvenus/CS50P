import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        if matches:= re.search(r'^((1[0-2]|[0-9]):?([0-5][0-9])? (AM|PM) to (1[0-2]|[0-9]):?([0-5][0-9])? (AM|PM))', s, re.IGNORECASE):
            hour1 = int(matches.group(2))
            minutes1 = matches.group(3)
            ampm1 = matches.group(4)
            hour2 = int(matches.group(5))
            minutes2 = matches.group(6)
            ampm2 = matches.group(7)
            minutes1 = minutes1 if minutes1 is not None else "00"
            minutes2 = minutes2 if minutes2 is not None else "00"
            if ampm1.upper() == "PM" and hour1 < 12:
                hour1 += 12
            elif ampm1.upper() == "AM" and hour1 == 12:
                hour1 = 0
            if ampm2.upper() == "PM" and hour2 <12:
                hour2 += 12
            elif ampm2.upper() == "AM" and hour2 == 12:
                hour2 = 0
            return (f"{hour1:02}:{minutes1} to {hour2:02}:{minutes2}")
        else:
            raise ValueError(sys.exit("ValueError"))
    except ValueError:
        sys.exit()

if __name__ == "__main__":
    main()