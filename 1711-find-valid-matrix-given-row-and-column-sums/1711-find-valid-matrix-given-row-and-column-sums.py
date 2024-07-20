class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        m=len(rowSum)
        n=len(colSum)
        an = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                val=min(rowSum[i],colSum[j])
                an[i][j]=val
                rowSum[i]-=val
                colSum[j]-=val
        return an

        