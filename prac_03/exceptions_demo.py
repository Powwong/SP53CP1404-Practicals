"""exceptions_demo"""

"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    - This will happen if you enter the letter not numbers
2. When will a ZeroDivisionError occur?
    - This error will happen if the denominator enters is 0 
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    - This can be by adding a while loop so that it will prevents zero  
    from being entered as a denominator
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be 0")
        denominator = int(input("Enter the denominator:"))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")