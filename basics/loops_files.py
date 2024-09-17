if False:
    coffee_varieties = ["capachino", "latte", "cold"]
    ingridients = {"solvent": "milk", "solute": "coffee"}
    for c in coffee_varieties:
        print(c, end="-")

    if "cold" in coffee_varieties:
        print("coooold")

    for i in ingridients:
        print(ingridients[i])

    for key, value in ingridients.items():
        print(key, value)

    for key in ingridients.keys():
        print(key)

    if "solvent" in ingridients:
        print("buy coffee")

    # problems
    # sum of even numbers till n
    n = int(input("give a number: "))
    even_sum = 0
    for i in range(n + 1):
        if i % 2 == 0:
            even_sum += i
    print(even_sum)

    # continue to skip iteration and break for exiting the iterations

    # reversing a string using loop
    str = "nice"
    newstr = ""
    for i in str:
        newstr = i + newstr
    print(newstr)

    # factorial
    x = 3
    f = 1
    while x > 0:
        f *= x
        x -= 1
    print(f)

    # when duplicate found exit the loop
    arr = ["what", "why", "when", "what"]
    unique = set()
    for item in arr:
        if item in unique:
            print("duplicate")
            break
        else:
            unique.add(item)
            print(item)

for line in open("chai.py"):
    # u may also see open('..').readlines() which is pretty haevy on memory
    print(line, end="")

f = open("chai.py")
# f is same as iter(f) and f.__iter__() for only files which means f is already an iterable object which wont be the case with other data types who holds the reference of the data location not the iterable object
while True:
    line = f.readline()
    # readline uses __next__()
    if not line:
        break
    print(line, end="")
