"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# FIXED

score = float(input("Enter score: "))
if score < 0 or score > 100:
    message = ("Invalid Score")
elif score < 50:
    message = ("Bad")
elif score < 90:
    message = ("Passable")
else:
    message = ("Excellent")

print(message)