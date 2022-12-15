def char_to_int(char):
    if char.islower():
        return ord(char) - 96
    return ord(char) - 38


def main():
    lines = [line.strip() for line in open("input", "r").readlines()]
    priority_sum = 0
    for line in lines:
        line = [c for c in line]
        first_half = set(line[0:len(line)//2])
        second_half = set(line[len(line)//2:len(line)])
        common = first_half.intersection(second_half)
        priority_sum += char_to_int(common.pop())
    print(f"Priority sum is: {priority_sum}")

    priority_sum = 0
    group = []
    for line in lines:
        group.append(set([c for c in line]))
        if len(group) == 3:
            common = group[0].intersection(group[1].intersection(group[2]))
            priority_sum += char_to_int(common.pop())
            group = []
    print(f"Priority sum for groups is: {priority_sum}")


if __name__ == "__main__":
    main()
