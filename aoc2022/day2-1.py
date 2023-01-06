with open("day2.txt", "r") as file:
    data = file.read()
    rps = data.split("\n")
    scores = []
    for match in rps:
        if match == "A X":
            scores.append(4)
        elif match == "A Y":
            scores.append(8)
        elif match == "A Z":
            scores.append(3)
        elif match == "B X":
            scores.append(1)
        elif match == "B Y":
            scores.append(5)
        elif match == "B Z":
            scores.append(9)
        elif match == "C X":
            scores.append(7)
        elif match == "C Y":
            scores.append(2)
        elif match == "C Z":
            scores.append(6)
    total = sum(scores)
    print("total score: {}".format(total))
