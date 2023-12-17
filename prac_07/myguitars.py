import csv
from prac_06.guitar import Guitar


guitars = []
class_guitars = []


def main():
    in_file = open('guitars.csv', 'r', newline='')
    in_file.readline()
    guitar = csv.reader(in_file)  # use default dialect, Excel
    for row in guitar:
        guitars.append(row)
    in_file.close()
    print("These are my guitars:")
    for guitar in guitars:
        class_guitars.append(Guitar(guitar[0], int(guitar[1]), float(guitar[2])))
    class_guitars.sort()
    for i, guitar in enumerate(class_guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")





main()