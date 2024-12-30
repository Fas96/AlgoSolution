class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = (10**9) + 7 
        dp={}
        def dfs(ln):
            if ln>high:
                return 0
            if ln in dp: return dp[ln]
            dp[ln]=1 if ln>=low else 0
            dp[ln]+=dfs(ln+zero)+dfs(ln+one)
            return dp[ln]%MOD
    
        return dfs(0)
