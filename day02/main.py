def round_result_score(opponent, self):
    # A / Y = Rock
    # B / X = Paper
    # C / Z = Scissors
    if opponent == "A":
        if self == "X":
            return 3
        if self == "Y":
            return 6
        if self == "Z":
            return 0
    if opponent == "B":
        if self == "X":
            return 0
        if self == "Y":
            return 3
        if self == "Z":
            return 6
    if opponent == "C":
        if self == "X":
            return 6
        if self == "Y":
            return 0
        if self == "Z":
            return 3


def chosen_shape_value(self):
    if self == "X":
        return 1
    if self == "Y":
        return 2
    if self == "Z":
        return 3


def which_shape_to_chose(opponent, outcome):
    if opponent == "A":
        if outcome == "X":
            return "Z"
        if outcome == "Y":
            return "X"
        if outcome == "Z":
            return "Y"
    if opponent == "B":
        if outcome == "X":
            return "X"
        if outcome == "Y":
            return "Y"
        if outcome == "Z":
            return "Z"
    if opponent == "C":
        if outcome == "X":
            return "Y"
        if outcome == "Y":
            return "Z"
        if outcome == "Z":
            return "X"


def main():
    lines = [line.strip() for line in open("input", "r").readlines()]
    score = 0
    for line in lines:
        opponent, self = line.split(" ")
        score += round_result_score(opponent, self)
        score += chosen_shape_value(self)
    print(f"Total score following first plan: {score}")

    score = 0
    for line in lines:
        opponent, outcome = line.split(" ")
        self = which_shape_to_chose(opponent, outcome)
        score += round_result_score(opponent, self)
        score += chosen_shape_value(self)
    print(f"Total score following second plan: {score}")



if __name__ == "__main__":
    main()
