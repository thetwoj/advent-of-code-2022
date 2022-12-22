from queue import Queue


class Monkey:
    def __init__(self):
        self.items = Queue()


def main():
    lines = [line.strip() for line in open("input", "r").readlines()]


if __name__ == "__main__":
    main()
