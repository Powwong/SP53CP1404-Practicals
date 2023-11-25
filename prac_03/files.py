"""files"""

OUTPUT_FILE = "name.txt"
INPUT_FILE = "name.txt"
total_number = 0

out_file = open(OUTPUT_FILE, 'w')
name = input("Input name: ")
print(name, file=out_file)
out_file.close()

in_file = open(INPUT_FILE, "r")
name = in_file.read()
print(f"Your name is {name}")
in_file.close()

in_file = open("numbers.txt", "r")
number = in_file.readlines()
total_number = int(number[0]) + int(number[1])
in_file.close()
print(total_number)

in_file = open("numbers.txt", "r")
number = in_file.readlines()
for i in range(0, len(number)):
    total_number += int(number[i])
in_file.close()
print(total_number)
