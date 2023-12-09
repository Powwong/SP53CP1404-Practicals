COLORS = {"": "", "Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "Alice Blue": "#f0f8ff", "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00", "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "	#eedfcc"}


def main():
    color_name = validate_color_name()
    while color_name != "":
        color_code = COLORS[color_name]
        print(f"{color_code}")
        color_name = validate_color_name()


def validate_color_name():
    color_name = input("Color Name: ").title()
    while color_name not in COLORS:
        print("Invalid Color Name")
        color_name = input("Color Name: ").title()
    return color_name


main()