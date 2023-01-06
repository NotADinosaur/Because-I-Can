with open("day1.txt", "r") as file:
    data = file.read()
    numList = data.split("\n")
    amount = 0
    sums = []
    for number in numList:
        if number == "":
            sums.append(amount)
            amount = 0
        else:
            amount = amount + int(number)
    sums = sorted(sums, reverse = True)
    largest = sums[0]
    second = sums[1]
    third = sums[2]
    topThree = largest + second + third
    print("amount of three largest: {}".format(topThree))
