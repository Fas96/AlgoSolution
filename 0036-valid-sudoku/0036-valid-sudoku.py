class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowHa=defaultdict(set)
        colHa=defaultdict(set)
        sq=defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                if board[i][j]==".":
                    continue
                if ((board[i][j] in rowHa[i]) or
                    (board[i][j] in colHa[j]) or
                    (board[i][j] in sq[(i//3,j//3)]) 
                   ):
                    return False
                rowHa[i].add(board[i][j])
                colHa[j].add(board[i][j])
                sq[(i//3,j//3)].add(board[i][j])
        return True
        
        