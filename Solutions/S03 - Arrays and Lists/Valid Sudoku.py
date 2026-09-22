class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            if not self.validate_row(board[i]):
                return False

        for j in range(9):
            col = [board[i][j] for i in range(9)]
            if not self.validate_row(col):
                return False

        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                box = [
                    board[i][j]
                    for i in range(row, row + 3)
                    for j in range(col, col + 3)
                ]

                if not self.validate_row(box):
                    return False

        return True

    def validate_row(self, row):
        row_nums = [n for n in row if n.isdigit()]

        if len(set(row_nums)) != len(row_nums):
            return False

        return True