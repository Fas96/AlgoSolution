class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def bk(nums, index, subset, res): 
            if index == len(nums):
                res.append(subset[:])
                return 
            subset.append(nums[index])
            bk(nums, index + 1, subset, res)
            subset.pop() 
            bk(nums, index + 1, subset, res)
 
        res = []
        bk(nums, 0, [], res)
        return res