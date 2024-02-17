class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=defaultdict(set)
        cols=defaultdict(set)
        squares=defaultdict(set)
        for i in range(9):
            for j in range(9):
                n=board[i][j]
                if n==".":
                    continue
                if (n in rows[i] or n in cols[j] or n in squares[(i//3,j//3)]):
                    return False
                rows[i].add(n)
                cols[j].add(n)
                squares[(i//3,j//3)].add(n)
        return True