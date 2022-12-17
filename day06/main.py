def main():
    line = [line.strip() for line in open("input", "r").readlines()][0]
    for x in range(4, len(line)):
        if len(set(line[x-4:x])) == 4:
            print(f"with 4 char requirements, start of packet is at {x}")
            break

    for x in range(14, len(line)):
        if len(set(line[x-14:x])) == 14:
            print(f"with 14 char requirement, start of packet is at {x}")
            break


if __name__ == "__main__":
    main()
