class Tree:
    def __init__(self, height):
        self.height = height
        self.visibility = {
            "north": None,
            "south": None,
            "east": None,
            "west": None,
        }
        self.neighbors = {
            "north": None,
            "south": None,
            "east": None,
            "west": None,
        }

    def determine_visibility(self, direction):
        if self.visibility[direction] is not None:
            return self.visibility[direction]
        if self.neighbors[direction] is None:
            self.visibility[direction] = True
            return True
        neighbor_visible = self.neighbors[direction].determine_visibility(direction)
        if not neighbor_visible:
            if self.neighbors[direction].height >= self.height:
                self.visibility[direction] = False
            else:
                self.visibility[direction] = is_tall_enough(self, self.neighbors[direction], direction)
        if neighbor_visible:
            if self.neighbors[direction].height < self.height:
                self.visibility[direction] = True
            else:
                self.visibility[direction] = False
        return self.visibility[direction]

    def is_visible(self):
        self.determine_visibility("north")
        self.determine_visibility("south")
        self.determine_visibility("east")
        self.determine_visibility("west")
        return True in self.visibility.values()

    def __repr__(self):
        return f"{self.height}, {self.is_visible()}"


def is_tall_enough(og_tree, tree, direction):
    if tree.neighbors[direction] is None:
        return True
    if tree.neighbors[direction].height >= og_tree.height:
        return False
    elif tree.neighbors[direction].height < og_tree.height:
        return is_tall_enough(og_tree, tree.neighbors[direction], direction)


def main():
    lines = [line.strip() for line in open("input", "r").readlines()]
    height = len(lines)
    width = len(lines[0])
    grid = [[Tree(0) for _ in range(width)] for _ in range(height)]
    for y, line in enumerate(lines):
        for x, tree_height in enumerate(line):
            tree = grid[y][x]
            tree.height = tree_height
            if y > 0:
                tree.neighbors["north"] = grid[y-1][x]
            if x > 0:
                tree.neighbors["west"] = grid[y][x-1]
            if y < height - 1:
                tree.neighbors["south"] = grid[y+1][x]
            if x < width - 1:
                tree.neighbors["east"] = grid[y][x+1]

    visible_tress = 0
    for row in grid:
        for tree in row:
            if tree.is_visible():
                visible_tress += 1

    # import pprint
    # pprint.pprint(grid)

    print(f"There are {visible_tress} visible trees")


if __name__ == "__main__":
    main()
