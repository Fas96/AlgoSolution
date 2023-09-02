class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        dict_set = set(dictionary)

        n = len(s)
        dp = [0] * (n + 1)

        for i in range(1, n + 1):
            dp[i] = dp[i - 1] + 1

            for j in range(i - 1, -1, -1):
                substring = s[j:i]
                if substring in dict_set:
                    dp[i] = min(dp[i], dp[j])

        return dp[n]