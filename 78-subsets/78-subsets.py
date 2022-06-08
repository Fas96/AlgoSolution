class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        size = len(nums)
        result = []
        for i in range(size):
            if i == 0:
                result = [[], [nums[i]]]
            else:
                result += [[nums[i]] + item for item in result]
            
        return result