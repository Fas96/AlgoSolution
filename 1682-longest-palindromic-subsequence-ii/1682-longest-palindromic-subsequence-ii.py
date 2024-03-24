class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def dfs(i,j,ch):
            if i >= j:
                return 0

            if s[i] == s[j] and s[i] != ch:
                return 2 + dfs(i+1,j-1,s[i])

            return max(dfs(i+1,j,ch),dfs(i,j-1,ch))

        res = dfs(0,n-1,"#")
       
        return res