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
        self.index = {}
        self.total_unmarked = 0
        self.marked_rows = [0] * 5
        self.marked_cols = [0] * 5

        for i, row in enumerate(self.rows):
            for j, val in enumerate(row):
                assert val not in self.index, "Dupes not allowed!"
                self.index[val] = (i, j)
                self.total_unmarked += val

    def handle_call(self, call):
        if call not in self.index:
            return
        i, j = self.index[call]
        self.marked_rows[i] += 1
        self.marked_cols[j] += 1
        self.total_unmarked -= call
        return self.marked_rows[i] == 5 or self.marked_cols[j] == 5


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
