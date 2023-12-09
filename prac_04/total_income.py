
def main():
    """Display income report for incomes over a given number of months."""
    incomes = []
    number_of_months = int(input("How many months? "))

    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {str(month)}: "))
        incomes.append(income)

    display_report(incomes, number_of_months)


def display_report(incomes, number_of_months):
    """This function will display a report of the income"""
    print("\nIncome Report\n-------------")
    total = 0
    for month in range(1, number_of_months + 1):
        income = incomes[month - 1]
        total += income
        print(f"{month:2} - Income: ${income:10.2f} Total: ${total:10.2f}")


main()