from collections import defaultdict

def move_head(direction, x, y):
    if direction == "R":
        return x+1, y
    if direction == "L":
        return x-1, y
    if direction == "U":
        return x, y+1
    if direction == "D":
        return x, y-1


def move_tail(hx, hy, tx, ty):
    # horizontal gap
    if hx == tx:
        if hy-2 == ty:
            return tx, ty+1
        if hy+2 == ty:
            return tx, ty-1
    # vertical gap
    if hy == ty:
        if hx-2 == tx:
            return tx+1, ty
        if hx+2 == tx:
            return tx-1, ty
    # diagonal gap
    if hx > tx and hy > ty:
        if hx > tx+1 or hy > ty+1:
            return tx+1, ty+1
    if hx > tx and hy < ty:
        if hx > tx+1 or hy < ty-1:
            return tx+1, ty-1
    if hx < tx and hy > ty:
        if hx < tx-1 or hy > ty+1:
            return tx-1, ty+1
    if hx < tx and hy < ty:
        if hx < tx-1 or hy < ty-1:
            return tx-1, ty-1
    # no change needed
    return tx, ty


def main():
    tail_positions = defaultdict(int)
    head_x, head_y = 0, 0
    tail_x, tail_y = 0, 0
    tail_positions[f"{tail_x}, {tail_y}"] += 1

    lines = [line.strip() for line in open("input", "r").readlines()]
    for line in lines:
        direction, count = line.split(" ")
        count = int(count)
        for _ in range(count):
            head_x, head_y = move_head(direction, head_x, head_y)
            tail_x, tail_y = move_tail(head_x, head_y, tail_x, tail_y)
            tail_positions[f"{tail_x}, {tail_y}"] += 1
            # print(f"HEAD: {head_x}, {head_y}")
            # print(f"TAIL: {tail_x}, {tail_y}")

    # from pprint import pprint
    # pprint(tail_positions)
    tail_position_count = len(tail_positions)
    print(f"Tail was in {tail_position_count} positions")


if __name__ == "__main__":
    main()
