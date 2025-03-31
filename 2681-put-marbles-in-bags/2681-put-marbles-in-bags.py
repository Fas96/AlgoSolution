class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int:
        n = len(weights)
        if k == 1:
            return 0
        
        diffs = []
        for i in range(n - 1):
            diffs.append(weights[i] + weights[i + 1])
        
        diffs.sort()
        
        return sum(diffs[-(k - 1):]) - sum(diffs[:k - 1])        