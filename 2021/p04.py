import sys

lines = [ln.strip() for ln in open(sys.argv[1])]

calls = [int(n) for n in lines.pop(0).split(",")]

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

    @classmethod
    def read_boards(cls, lines):
        boards = []
        lines = iter(lines)
        while True:
            try:
                boards.append(cls.read_board(lines))
            except StopIteration:
                break
        return boards

    @classmethod
    def read_board(cls, lines):
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
        self.total_unmarked -= call
        return all(self.marked[i]) or all(self.marked[y][j] for y in range(5))


def find_first_winning_score(boards, calls):
    for call in calls:
        for board in boards:
            result = board.handle_call(call)
            if result:
                return board.total_unmarked * call

# part 1: 38594
boards = Board.read_boards(lines)
print(find_first_winning_score(boards, calls))

# part 2: 21184
def find_last_winning_score(boards, calls):
    calls = iter(calls)
    while boards:
        call = next(calls)
        board = boards[0]  # save in case it's the last one
        boards = [b for b in boards if not b.handle_call(call)]
    return board.total_unmarked * call


boards = Board.read_boards(lines)
print(find_last_winning_score(boards, calls))
