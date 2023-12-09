MENUS = """(H)ello 
(G)oodbye 
(Q)uit
"""

name = input("Enter name: ")
print(MENUS, end=" ")
choice = input(">>>").upper()
while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid")
    print(MENUS, end=" ")
    choice = input(">>>").upper()
print("Finished")