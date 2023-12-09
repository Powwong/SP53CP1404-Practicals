"""SCORE_MENU"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit
"""

def main():
    score = validate_score()
    print(MENU, end="")
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "G":
            score = validate_score()
        elif choice == "P":
            score_state = determine_score(score)
            print(score_state)
        elif choice == "S":
            display_stars(score)
        else:
            print("Invalid Choice")
        print(MENU, end="")
        choice = input(">>>").upper()
    print("Goodbye")


def display_stars(score):
    print("*" * score)


def determine_score(score):
    if score < 50:
        score_state = "Bad"
    elif score < 90:
        score_state = "Passable"
    else:
        score_state = "Excellent"
    return score_state


def validate_score():
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid Score")
        score = int(input("Score: "))
    return score


main()