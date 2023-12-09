NAMES = {}
COUNTRIES = {}
champions = []
countries = []


def main():
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        data = in_file.readlines()
        extract_data(data)
        count_add_dictionary(champions, NAMES)
        print("Wimbledon Champions: ")
        for name in NAMES.keys():
            print(f"{name}: {NAMES[name]}")
        count_add_dictionary(countries, COUNTRIES)
        sorted_countries = sort_list(COUNTRIES)
        print(f"These {len(sorted_countries)} countries have won the Wimbledon:")
        print(", ".join(sorted_countries))


def sort_list(dictionary):
    list_current = dictionary.keys()
    sorted_list = sorted(list_current)
    return sorted_list


def extract_data(data):
    for line in data[1:]:
        items = line.strip().split(",")
        champions.append(items[2])
        countries.append(items[1])


def count_add_dictionary(list_name, dictionary_name):
    for item in list_name:
        if item in dictionary_name.keys():
            dictionary_name[item] += 1
        else:
            dictionary_name[item] = 1


main()