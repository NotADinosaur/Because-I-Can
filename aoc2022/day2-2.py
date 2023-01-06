with open("day2.txt", "r") as file:
    data = file.read()
    rps = data.split("\n")
    scores = []
    for match in rps:
        if "X" in match:
            if "A" in match:
                scores.append(3)
            elif "B" in match:
                scores.append(1)
            elif "C" in match:
                scores.append(2)
        elif "Y" in match:
            if "A" in match:
                scores.append(4)
            elif "B" in match:
                scores.append(5)
            elif "C" in match:
                scores.append(6)
        elif "Z" in match:
            if "A" in match:
                scores.append(8)
            elif "B" in match:
                scores.append(9)
            elif "C" in match:
                scores.append(7)
    total = sum(scores)
    print("total score: {}".format(total))
