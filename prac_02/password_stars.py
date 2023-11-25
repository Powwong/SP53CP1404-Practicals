""""PASSWORD_STARS"""


MINIMUM_LENGTH = 3


def main():
    password_output = validate_password()
    display_password(password_output)


def display_password(password_output):
    """ This function is for displaying the star output"""
    print("*" * password_output)


def validate_password():
    """This function is for validating the inputted password"""
    password = input("Password: ")
    password_output = len(password)
    while password_output < MINIMUM_LENGTH:
        print("Password length too short")
        password = input("Password: ")
        password_output = len(password)
    return password_output


main()