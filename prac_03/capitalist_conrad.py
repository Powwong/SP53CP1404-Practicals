"""capitalist_conrad"""

"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""

import random

MAX_INCREASE = 0.175
MAX_DECREASE = 0.05
MIN_PRICE = 1
MAX_PRICE = 100
INITIAL_PRICE = 10.0
OUTPUT_FILE = "capitalist.txt"
numbers_of_days = 0


price = INITIAL_PRICE
print(f"Starting price : ${price:,.2f}")

out_file = open(OUTPUT_FILE, 'w')

while MIN_PRICE <= price <= MAX_PRICE:
    price_change = 0
    # this will generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # this will generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # this will generate a random floating-point number
        # between 0 and MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)
    numbers_of_days += 1

    price *= (1 + price_change)
    print(f"On day {numbers_of_days} price is ${price:,.2f}", file=out_file)
    print(f"On day {numbers_of_days} price is ${price:,.2f}")
out_file.close()