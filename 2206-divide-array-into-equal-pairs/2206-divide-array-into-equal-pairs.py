class Solution(object):
    def divideArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums.sort()
        db = len(nums) // 2

        for i in range(0, len(nums), 2):
            if nums[i:i + 2][0]!=nums[i:i + 2][1]:
                return  False
        return True
