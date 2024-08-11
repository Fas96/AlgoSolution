class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n=len(s)
        dp=[True]
        for i in range(1,n+1):
            dp.append(any(dp[j] and s[j:i] in wordDict for j in range(i)))
        return dp[-1]
        