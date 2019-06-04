print("DOT PRODUCT CALCULATOR by Greg Brown")
print()

n = input("input vector dimension: ")

while type(n) != type(1):
    try:
        n = int(n)
    except ValueError:
        print()
        print("error: the input was not an integer. enter an integer.")
        n = input("input vector dimension: ")

v1 = []
v2 = []

print()
print("list the entries of the first vector: ")

for i in range(n):
    entry = input()
    while type(entry) != type(1.1):
        try:
            entry = float(entry)
        except ValueError:
            print()
            print("error: the input was not a decimal number. enter a number.")
            entry = input("list the entries of the first vector: ")
    v1.append(entry)

print("vector one: " + str(v1))

print()
print("now list the entries of the second vector: ")

for i in range(n):
    entry = input()
    while type(entry) != type(1.1):
        try:
            entry = float(entry)
        except ValueError:
            print()
            print("error: the input was not a decimal number. enter a number.")
            entry = input("list the entries of the second vector: ")
    v2.append(entry)

print("vector two: " + str(v2))

product_list = [i*j for i, j in zip(v1, v2)]

print()
print()

if n >= 8:
    print(str(v1))
    print("+")
    print(str(v2))
    print("=")
    print(str(sum(product_list)))
else:
    print(str(v1) + " * " + str(v2) + " = " + str(sum(product_list)))

print()
input("press enter to exit.")
