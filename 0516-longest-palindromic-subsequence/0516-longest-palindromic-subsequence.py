class Solution:
    def longestPalindromeSubseq(self, word1: str) -> int:
        word2 = word1[::-1]
        m, n = len(word1), len(word2)

        @lru_cache(None)
        def lcs(i, j):
            if i == m or j == n:
                return 0
            if word1[i] == word2[j]:
                return 1 + lcs(i + 1, j + 1)
            return max(lcs(i + 1, j), lcs(i, j + 1))
        
        return lcs(0, 0)
        