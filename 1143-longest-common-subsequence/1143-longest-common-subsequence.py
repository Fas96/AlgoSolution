from collections import Counter
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        n = len(text1)
        m = len(text2)
        # dp = [[0] * (len(text2) + 1)] * (len(text1) + 1)
        mx = 0
        dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]
    
        for j in range(0,m+1):
            dp[0][j] = 0
        for i in range(0,n+1):
            dp[i][0] = 0
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = 1 + (dp[i - 1][j - 1])
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        return dp[n][m]