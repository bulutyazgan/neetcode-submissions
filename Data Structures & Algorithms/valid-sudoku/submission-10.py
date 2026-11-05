class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)

        for row in range(9):
            for col in range(9):
                x = board[row][col]
                if x == ".":
                    continue
                if x in rows[row]:
                    return False
                if x in cols[col]:
                    return False
                rows[row].add(x)
                cols[col].add(x)

                square = (row // 3) * 3 + (col // 3)
                if x in squares[square]:
                    return False
                squares[square].add(x)
        return True
