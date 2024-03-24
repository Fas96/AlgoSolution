class Solution:
    def minOperations(self, k: int) -> int:
        best = k - 1
        
        for i in range(k):
            best = min(best, max(0, (k + i) // (i + 1) - 1) + i)
        return best