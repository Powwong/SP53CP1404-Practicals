"""SCORE"""


import random


def main():
    score = float(input("Enter score: "))
    score_state = determine_score(score)
    print(score_state)
    print(determine_score(random.randint(0, 100)))


def determine_score(score):
    """This function is to determine the grade of a score"""
    if score < 0 or score > 100:
        score_state = "Invalid Score"
    elif score < 50:
        score_state = "Bad"
    elif score < 90:
        score_state = "Passable"
    else:
        score_state = "Excellent"
    return score_state


main()