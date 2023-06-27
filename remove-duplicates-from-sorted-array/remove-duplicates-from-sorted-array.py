class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx=1
        while idx < len(nums):
            if nums[idx]==nums[idx-1]:
                nums.pop(idx)
            else:
                idx+=1
        return idx
        