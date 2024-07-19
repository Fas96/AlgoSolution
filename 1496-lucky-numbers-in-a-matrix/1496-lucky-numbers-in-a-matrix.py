class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        m,n=len(matrix),len(matrix[0])
        ans=[]
        def rc(matrix, i, j):
            row = matrix[i]
            col = [row[j] for row in matrix]
            return min(row), max(col)
        for i in range(m): 
            for j in range(n): 
                row,col=rc(matrix,i,j) 
                if  row == col: ans+=[col]
                
        return ans 