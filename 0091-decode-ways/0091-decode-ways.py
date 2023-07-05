class Solution:
    def numDecodings(self, s: str) -> int:
        
        dp = [0] * (len(s) + 1)

        dp[len(s)] = 1
        dp[len(s) - 1] = 1 if s[len(s) - 1] != '0' else 0

        for i in range(len(s) - 2, -1, -1):
            if s[i] == '0':
                continue
            else:
                dp[i] = dp[i + 1] + dp[i + 2] if int(s[i:i + 2]) <= 26 else dp[i + 1]

        return dp[0]
        