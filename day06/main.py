class FSDir:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.children = []

    @property
    def size(self):
        total = 0
        for child in self.children:
            total += child.size
        return total

    @property
    def fullpath(self):
        if self.parent is None:
            return ""
        return f"{self.parent.fullpath}/{self.name}"


class FSFile:
    def __init__(self, name, size, parent):
        self.name = name
        self.size = size
        self.parent = parent


def change_dir(dirs, current_dir, target_dir):
    if target_dir == "..":
        return current_dir.parent
    if target_dir == "/":
        path = "/"
    else:
        path = f"{current_dir.fullpath}/{target_dir}"
    return dirs[path]


def main():
    lines = [line.strip() for line in open("input", "r").readlines()]
    current_dir = FSDir("/", None)
    dirs = {current_dir.name: current_dir}
    for line in lines:
        if not line.startswith("$"):
            if line.startswith("dir"):
                name = line.split(" ")[1]
                if name in dirs:
                    print(name, dirs)
                    continue
                new_dir = FSDir(name, current_dir)
                current_dir.children.append(new_dir)
                dirs[new_dir.fullpath] = new_dir
            else:
                size, name = line.split(" ")
                size = int(size)
                current_dir.children.append(FSFile(name, size, current_dir))
        if line.startswith("$ cd"):
            current_dir = change_dir(dirs, current_dir, line[5:])

    total = 0
    for d in dirs.values():
        if d.size < 100000:
            total += d.size
    print(f"Total size of all dirs with size < 100000: {total}")
    root_size = dirs["/"].size
    print(f"Total size of filesystem: {root_size}")
    free_space = 70000000 - root_size
    print(f"Free space: {free_space}")

    # max 70000000
    # desired free 30000000
    min_to_delete = 30000000 - free_space
    print(f"Min to delete: {min_to_delete}")
    large_enough = {}
    for d in dirs.values():
        if d.size > min_to_delete:
            large_enough[d.size] = d
    print(f"Size of smallest dir that would work: {min(large_enough)}")


if __name__ == "__main__":
    main()
