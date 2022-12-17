import copy


def one_at_a_time(stacks, source, dest):
    stacks[dest].append(stacks[source].pop())


def grouped(stacks, count, source, dest):
    temp = []
    for _ in range(count):
        temp.append(stacks[source].pop())
    temp.reverse()
    print(temp)
    stacks[dest] += temp


def main():
    stacks = []
    crate_input = []
    lines = [line.rstrip() for line in open("input", "r").readlines()]
    crates = True
    steps = False
    for line in lines:
        if not line:
            steps = True
            continue
        if line.startswith(" 1"):
            crates = False
            while crate_input:
                crate_start_position = crate_input.pop()
                for idx, crate in enumerate(crate_start_position):
                    if crate == " ":
                        continue
                    if idx > len(stacks) - 1:
                        for x in range(len(stacks)-1, idx):
                            stacks.append([])
                    stacks[idx].append(crate)
            import pprint
            pprint.pprint(stacks)
            stacks_copy = copy.deepcopy(stacks)
            continue
        if crates:
            t = []
            for x in range(1, len(line), 4):
                t.append(line[x])
            crate_input.append(t)
            continue
        if steps:
            words = line.split(" ")
            count, source, dest = int(words[1]), int(words[3])-1, int(words[5])-1
            for _ in range(count):
                one_at_a_time(stacks, source, dest)
            grouped(stacks_copy, count, source, dest)
    import pprint
    print("Final stacks:")
    pprint.pprint(stacks)
    top_letters = []
    for stack in stacks:
        top_letters.append(stack[-1])
    top_word = "".join(top_letters)
    print(f"Top crates spell: {top_word}")

    print("Final grouped stacks:")
    pprint.pprint(stacks_copy)
    top_letters = []
    for stack in stacks_copy:
        top_letters.append(stack[-1])
    top_word = "".join(top_letters)
    print(f"Top grouped crates spell: {top_word}")


if __name__ == "__main__":
    main()
