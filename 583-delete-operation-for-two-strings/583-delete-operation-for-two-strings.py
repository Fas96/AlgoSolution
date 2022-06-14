class Solution(object):
    def minDistance(self, word1, word2):

        mx = len(word2)
        mi = len(word1)

        dp = [[0] * (mx + 1) for i in range(mi + 1)]
        for i in range(mi):
            for j in range(mx):
                if word1[i] == word2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        return (mi + mx) - (2 * dp[-1][-1])