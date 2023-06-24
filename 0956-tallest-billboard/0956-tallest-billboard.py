class Solution:
    def tallestBillboard(self, rods: List[int]) -> int: 
        dp = {0: 0}
        for r in rods: 
            for k, v in list(dp.items()): 
                dp[k+r] = max(dp.get(k+r, 0), v+r) 
                dp[k-r] = max(dp.get(k-r, 0), v)
      
        return dp[0]
        