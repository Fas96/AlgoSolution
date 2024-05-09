class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        
        
        h = sorted(happiness, reverse = True)
        res = 0
        for i in range(k):
            if h[i] <= i:
                return res
            res += h[i] - i
        return res
            
            