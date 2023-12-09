import random
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

quick_pick_number = int(input("How many quick picks?"))
for i in range(0, quick_pick_number):
    random_numbers = []
    for j in range(0, 6):
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        random_numbers.append(number)
        filtered_numbers = []
        while [filtered_numbers.append(number_removed) for number_removed in random_numbers if number_removed not in filtered_numbers]:
            [filtered_numbers.append(random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)) for x in random_numbers if len(filtered_numbers) < 6]
    print(str(filtered_numbers)[1:-1].replace(",", " "))