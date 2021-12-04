import sys

lines = (ln.strip() for ln in open(sys.argv[1]))

calls = [int(n) for n in next(lines).split(",")]
row_groups = []
for _ in lines:  # skips blank separator
    rows = []
    for _ in range(5):
        rows.append([int(n) for n in next(lines).split()])
    row_groups.append(rows)


class Board:
    def __init__(self, rows):
        self.rows = rows
        self.marked = [[0] * len(rows[0]) for _ in range(len(rows))]

        # assumes each number appears at most once per board
        self.index = {}
        self.total_unmarked = 0
        for i, row in enumerate(self.rows):
            for j, val in enumerate(row):
                self.index[val] = (i, j)
                self.total_unmarked += val

    def handle_call(self, call):
        if call not in self.index:
            return
        i, j = self.index[call]
        self.marked[i][j] = 1
        self.total_unmarked -= call
        return all(self.marked[i]) or all(self.marked[y][j] for y in range(5))


def find_wins(row_groups, calls):
    boards = [Board(rows) for rows in row_groups]
    calls = iter(calls)
    while boards:
        call = next(calls)
        next_boards = []
        for board in boards:
            win = board.handle_call(call)
            if win:
                yield board.total_unmarked * call
            else:
                next_boards.append(board)
        boards = next_boards


# part 1: 38594
print(next(find_wins(row_groups, calls)))

# part 2: 21184
for win in find_wins(row_groups, calls):
    pass
print(win)
