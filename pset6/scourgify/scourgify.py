import sys
import csv

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
else:
    try:
        with open(sys.argv[1]) as before, open(sys.argv[2],"w") as after:
            reader = csv.DictReader(before)
            writer = csv.DictWriter(after, fieldnames =["first","last","house"])
            writer.writeheader()
            for row in reader:
                last, first = row["name"].split(",")
                last,first = last.strip(),first.strip()
                writer.writerow({"first":first,"last":last,"house":row["house"]})

    except FileNotFoundError:
        sys.exit("Could not read invalid_file.csv")