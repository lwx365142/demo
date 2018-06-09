def whi():
    i = 0
    numbers = []

    while i < 6:
        print("At the top is %d" % i )
        numbers.append(i)

        i = i + 1
        print("Number now:",  numbers)
        print("At the bottle is %d" % i)

    print("The number is:")
    for num in numbers:
        print(num)
whi()

