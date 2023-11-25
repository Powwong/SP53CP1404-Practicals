LOW_BONUS = 0.1
HIGH_BONUS = 0.15
SALES_LIMIT = 1000

sales = float(input("How much are your sales: $"))
while sales > 0:
    if sales > SALES_LIMIT:
        bonus = sales*LOW_BONUS
    else:
        bonus = sales*HIGH_BONUS
    print(f"Your bonus is {bonus:.2f}")
    sales = float(input("How much are your sales: $"))
