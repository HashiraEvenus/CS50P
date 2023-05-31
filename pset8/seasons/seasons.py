from datetime import date, datetime
import sys
import inflect

p = inflect.engine()

def main():

    birth = get_date()
    today = date.today()
    d = round((today - birth).total_seconds()/60)
    d = p.number_to_words(d,andword="").capitalize()
    print(d, "minutes")


def get_date():
    try:
        bday = input("Date of Birth: ")
        bday = datetime.strptime(bday, '%Y-%m-%d').date()
        return bday

    except ValueError:
        sys.exit("Provide correct form of date")
#def subtract(today,birth):



if __name__ == "__main__":
    main()