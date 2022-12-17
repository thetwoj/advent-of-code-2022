def to_set(str):
    start, end = str.split('-')
    start = int(start)
    end = int(end) + 1
    return set(x for x in range(start, end))


def main():
    lines = [line.strip() for line in open("input", "r").readlines()]
    wholly_contained = 0
    intersecting = 0
    for line in lines:
        raw1, raw2 = line.split(',')
        set1 = to_set(raw1)
        set2 = to_set(raw2)
        longest = max([len(set1), len(set2)])
        if len(set1.union(set2)) == longest:
            wholly_contained += 1
        if len(set1.intersection(set2)) > 0:
            intersecting += 1
    print(f"There are {wholly_contained} pairs where one contains the other")
    print(f"There are {intersecting} pairs that intersect at all")


if __name__ == "__main__":
    main()
