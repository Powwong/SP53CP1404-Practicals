EMAILS = {}


def main():
    email = validate_email()
    name = process_email(email)
    while email != "":
        choice = input(f'Is your name {name}? (Y/n)').upper()
        if choice == "Y":
            EMAILS[email] = name
        else:
            modified_name = input("Name: ")
            EMAILS[email] = modified_name
        email = validate_email()
        name = process_email(email)
    display_emails()


def display_emails():
    for email in EMAILS:
        print(f"{EMAILS[email]} ({email})")


def process_email(email):
    names = email.split("@")
    if "." in names[0]:
        name = names[0].split(".")
        final_name = " ".join(name).title()
        return final_name
    else:
        name = names[0].title()
        return name


def validate_email():
    email = input("Email: ")
    if email == "":
        return email
    while "@" not in email:
        print("Must be Valid Email")
        email = input("Email: ")
    return email

main()