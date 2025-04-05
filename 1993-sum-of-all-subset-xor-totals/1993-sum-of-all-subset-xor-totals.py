class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
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
        result = 0
        for s in res:
            st = 0
            for num in s:
                st ^= num
            result += st

        return result 