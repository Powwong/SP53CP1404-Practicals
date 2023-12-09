FILENAME = "subject_data.txt"


def main():
    input_file = get_data()
    data = process_data(input_file)
    display_data(data)


def get_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(FILENAME, "r")
    data = input_file.readlines()
    input_file.close()
    return data


def process_data(input_file):
    """This function is to process the data"""
    datas = []
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        print("\n")
        datas.append(parts)
    return datas


def display_data(parts):
    for line in parts:
        print(f"{line[0]} is taught by {line[1]} and has {line[2]} students")
    print("----------")


main()