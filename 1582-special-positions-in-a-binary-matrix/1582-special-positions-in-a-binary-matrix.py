class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        n=len(mat)
        m=len(mat[0])
        cnt=0
        transMat=list(zip(*mat))
        
        return sum(mat[i][j]==1 and sum(mat[i])==1 and sum(transMat[j])==1 for j in range(m) for i in range(n) )