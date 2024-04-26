class Solution:
    def minFallingPathSum(self, g: List[List[int]]) -> int:
        l=len(g)
        for i in range(1,l):
            temp =  sorted(g[i-1])
            for j in range(l):
                if g[i-1][j] == temp[0]:
                    g[i][j] += temp[1]
                else:
                    g[i][j] += temp[0]
        return min(g[-1])