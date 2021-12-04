import sys

lines = (ln.strip() for ln in open(sys.argv[1]))

calls = [int(n) for n in next(lines).split(",")]

class Board:
    def __init__(self, rows):
        self.rows = rows
        self.marked = [[0] * len(rows[0]) for _ in range(len(rows))]

        # assumes each number appears at most once per board
        self.index = {}
        for i, row in enumerate(self.rows):
            for j, val in enumerate(row):
                self.index[val] = (i, j)

    @classmethod
    def read_board(cls):
        next(lines)  # blank line
        rows = []
        for _ in range(5):
            rows.append([int(n) for n in next(lines).split()])
        return cls(rows)

    def handle_call(self, call):
        if call not in self.index:
            return
        i, j = self.index[call]
        self.marked[i][j] = 1
        return all(self.marked[i]) or all(self.marked[y][j] for y in range(5))

    def sum_unmarked(self):
        total = 0
        for i, row in enumerate(self.rows):
            for j, val in enumerate(row):
                if not self.marked[i][j]:
                    total += val
        return total

def read_boards():
    boards = []
    while True:
        try:
            boards.append(Board.read_board())
        except StopIteration:
            break
    return boards

def find_winning_score(boards, calls):
    for call in calls:
        for board in boards:
            result = board.handle_call(call)
            if result:
                return board.sum_unmarked() * call

# part 1: 38594
boards = read_boards()
print(find_winning_score(boards, calls))

