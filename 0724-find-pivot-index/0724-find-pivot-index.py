class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        idx=-1
        for i in range(len(nums)):
            # print(nums[i+1:],nums[:i])
            if sum(nums[i+1:])==sum(nums[:i]):
                return i
        return idx
        