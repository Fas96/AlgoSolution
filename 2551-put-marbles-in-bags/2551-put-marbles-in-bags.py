class Solution:
    def putMarbles(self, weights: List[int], k: int) -> int: 
        
        if k == 1 or k == len(weights):
            return 0
        sortedWeight = sorted(weights[i] + weights[i + 1] for i in range(len(weights) - 1))
        print(sortedWeight)
        return sum(sortedWeight[-k + 1:]) - sum(sortedWeight[:k - 1])
        