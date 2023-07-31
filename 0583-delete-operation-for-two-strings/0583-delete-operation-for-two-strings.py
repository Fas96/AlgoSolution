class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        
        @lru_cache(None)
        def lcs(i, j):
            if i == m or j == n:
                return 0
            if word1[i] == word2[j]:
                return 1 + lcs(i + 1, j + 1)
            return max(lcs(i + 1, j), lcs(i, j + 1))
        tt_lcs= lcs(0, 0)
        return m + n - 2 * tt_lcs 