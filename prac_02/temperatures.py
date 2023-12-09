"""TEMPERATURE"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = convert_celsius_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = convert_fahrenheit_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def convert_fahrenheit_celsius(fahrenheit):
    """This function is for converting inputted fahrenheit value into celsius"""
    celsius = 5 / 9 * (fahrenheit - 32)
    return celsius


def convert_celsius_fahrenheit(celsius):
    """This function is for converting celsius value into fahrenheit"""
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


main()