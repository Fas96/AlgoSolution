class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        if poured==query_row and query_row==query_glass:
            return 0
        dp = defaultdict(Counter)
        dp[0][0] = poured
        
        for i in range(query_row+1):
            for j in range(100):
                if j <= i-1:
                    dp[i][j] += max((dp[i-1][j]-1)/2, 0)
                if j:
                    dp[i][j] += max((dp[i-1][j-1]-1)/2, 0)

        return min(dp[query_row][query_glass], 1)
        
        