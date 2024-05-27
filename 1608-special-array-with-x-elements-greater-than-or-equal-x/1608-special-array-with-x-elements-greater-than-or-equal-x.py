 
class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort() 
        N = len(nums)
        for idx in range(N + 1): 
            if (N - bisect_left(nums, idx)) == idx: return idx
        return -1
        