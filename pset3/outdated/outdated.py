def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        try:
            date = input("Date: ").strip()
            if ',' in date:
                month, day, year = date.split(sep=' ')
                day = day.replace(",","")
            else:
                month, day, year = date.split(sep='/')
                if month in months:
                    raise ValueError

            if month in months:
                month = months.index(month)+1
            if (int(day)<31) and (int(month) <= len(months)):
                print(year,f"{int(month):02}",f"{int(day):02}", sep="-")
                break
            else:
                raise ValueError

        except ValueError:
            pass
main()




