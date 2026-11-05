class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen = set()
            for c in range(9):
                x = board[r][c]
                if x == ".": continue
                if x in seen: return False
                seen.add(x)
        for c in range(9):
            seen = set()
            for r in range(9):
                x = board[r][c]
                if x == ".": continue
                if x in seen: return False
                seen.add(x)
        for square in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    r = (square // 3) * 3 + i
                    c = (square % 3) * 3 + j
                    x = board[r][c]
                    if x == ".":
                        continue
                    if x in seen:
                        return False
                    seen.add(x)
        return True