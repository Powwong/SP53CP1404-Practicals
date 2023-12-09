"""A"""
for i in range(0, 101, 10):
    print(i, end=' ')
print()

"""B"""
for i in range(20, 0, -1):
    print(i, end=' ')
print()

"""C"""
stars = int(input("Number of stars: "))
for i in range(0, stars):
    print('*', end='  ')
print()

"""D"""
stars = int(input("Number of stars: "))
for i in range(1, stars+1):
    print("*"*i)
