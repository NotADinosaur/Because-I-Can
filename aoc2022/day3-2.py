with open("day3.txt", "r") as file:
    data = file.read()
    contents = data.split("\n")
    duplicates = []
    count = 0
    x = 0
    y = 1
    z = 2
    while count < len(contents)/3:
        first = set(contents[x])
        second = set(contents[y])
        third = set(contents[z])
        same = (first&second&third).pop()
        if same == "a":
            same = 1
        elif same == "b":
            same = 2
        elif same == "c":
            same = 3
        elif same == "d":
            same = 4
        elif same == "e":
            same = 5
        elif same == "f":
            same = 6
        elif same == "g":
            same = 7
        elif same == "h":
            same = 8
        elif same == "i":
            same = 9
        elif same == "j":
            same = 10
        elif same == "k":
            same = 11
        elif same == "l":
            same = 12
        elif same == "m":
            same = 13
        elif same == "n":
            same = 14
        elif same == "o":
            same = 15
        elif same == "p":
            same = 16
        elif same == "q":
            same = 17
        elif same == "r":
            same = 18
        elif same == "s":
            same = 19
        elif same == "t":
            same = 20
        elif same == "u":
            same = 21
        elif same == "v":
            same = 22
        elif same == "w":
            same = 23
        elif same == "x":
            same = 24
        elif same == "y":
            same = 25
        elif same == "z":
            same = 26
        elif same == "A":
            same = 27
        elif same == "B":
            same = 28
        elif same == "C":
            same = 29
        elif same == "D":
            same = 30
        elif same == "E":
            same = 31
        elif same == "F":
            same = 32
        elif same == "G":
            same = 33
        elif same == "H":
            same = 34
        elif same == "I":
            same = 35
        elif same == "J":
            same = 36
        elif same == "K":
            same = 37
        elif same == "L":
            same = 38
        elif same == "M":
            same = 39
        elif same == "N":
            same = 40
        elif same == "O":
            same = 41
        elif same == "P":
            same = 42
        elif same == "Q":
            same = 43
        elif same == "R":
            same = 44
        elif same == "S":
            same = 45
        elif same == "T":
            same = 46
        elif same == "U":
            same = 47
        elif same == "V":
            same = 48
        elif same == "W":
            same = 49
        elif same == "X":
            same = 50
        elif same == "Y":
            same = 51
        elif same == "Z":
            same = 52
        duplicates.append(same)
        count = count + 1
        x = x + 3
        y = y + 3
        z = z + 3
    total = sum(duplicates)
    print("sum: " + str(total))
