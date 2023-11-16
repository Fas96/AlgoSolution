class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        prev = 1
        for num in sorted(arr)[1:]:
            prev = min(prev + 1, num)
        
        return prev
        