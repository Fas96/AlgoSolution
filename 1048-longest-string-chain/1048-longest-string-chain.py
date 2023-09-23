class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        words.sort(key=len)
        def isSubsequence(s ,t):
            i, j = 0, 0
            while i < len(s) and j < len(t):
                if s[i] == t[j]:
                    i += 1
                j += 1
            return i == len(s)
        dp = [1] * len(words)
        for i in range(len(words)):
            for j in range(i):
                if len(words[i]) - len(words[j]) == 1 and isSubsequence(words[j], words[i]):
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)
                