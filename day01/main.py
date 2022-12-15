def main():
    lines = [line.strip() for line in open("input", "r").readlines()]

    calories_to_index = {}
    elf_index = 1
    calories = 0
    for line in lines:
        if line == "":
            calories_to_index[calories] = elf_index
            elf_index += 1
            calories = 0
            continue
        calories += int(line)
    calories_to_index[calories] = elf_index

    highest = max(calories_to_index)
    elf = calories_to_index[highest]
    print(f"Max calories: {highest}")
    print(f"Elf: {elf}")

    del calories_to_index[highest]
    second_highest = max(calories_to_index)
    del calories_to_index[second_highest]
    third_highest = max(calories_to_index)
    top_3_total = highest + second_highest + third_highest
    print(f"Sum of top 3 calories: {top_3_total}")


if __name__ == '__main__':
    main()
