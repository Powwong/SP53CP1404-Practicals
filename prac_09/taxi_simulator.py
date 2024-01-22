from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]


def main():
    taxi_choice = None
    bill_to_date = 0.0
    print(MENU)
    choice = input(">>>").lower()
    while choice != 'q':
        if choice == 'c':
            display_taxis()
            taxi_choice = validate_taxi_choice()
            if taxi_choice is not None:
                taxis[taxi_choice].start_fare()
        elif choice == 'd':
            if taxi_choice is None:
                print("You need to choose a taxi before you can drive")
            else:
                distance = int(input("Drive how far? "))
                taxis[taxi_choice].drive(distance)
                print(f"Your {taxis[taxi_choice].name} trip cost you {taxis[taxi_choice].get_fare()}")
                bill_to_date += taxis[taxi_choice].get_fare()
        else:
            print("Invalid Input")
        print(f"Bill to date: ${bill_to_date: .2f}")
        print(MENU)
        choice = input(">>>").lower()
    print(f"Total trip cost: {bill_to_date}")
    display_taxis()


def display_taxis():
    print("Taxis Available:")
    for i in range(0, len(taxis)):
        print(f"{i} - {taxis[i]}")


def validate_taxi_choice():
    index = input("Choose taxi: ")
    while not index.isdigit() or int(index) < 0 or int(index) > len(taxis) - 1:
        index = input("Choose taxi: ")
    return int(index)


main()