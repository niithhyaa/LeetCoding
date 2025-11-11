class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s1 = set()
        s2 = set()
        for i in range(9):
            s1.clear()
            s2.clear()
            for j in range(9):
                if board[i][j] in s1:
                    return False
                if board[j][i] in s2:
                    return False
                if board[i][j] != ".":
                    s1.add(board[i][j])
                if board[j][i] != ".":
                    s2.add(board[j][i])
        for sq in range(9):
            s1.clear()
            for i in range(3):
                for j in range(3):
                    row = (sq//3)*3 + i
                    col = (sq%3)*3 + j
                    if board[row][col] in s1:
                        return False
                    if board[row][col] != ".":
                        s1.add(board[row][col])
        return True
