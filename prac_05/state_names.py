lengths = []
# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code not in CODE_TO_NAME:
        raise Exception("Invalid Short State")
    else:
        print(state_code, "is", CODE_TO_NAME[state_code])
    state_code = input("Enter short state: ").upper()

for keys in CODE_TO_NAME.keys():
    length = len(keys)
    lengths.append(length)
    width = max(lengths)

for state_code in CODE_TO_NAME:
    print(f"{state_code: <{width}} is {CODE_TO_NAME[state_code]}")