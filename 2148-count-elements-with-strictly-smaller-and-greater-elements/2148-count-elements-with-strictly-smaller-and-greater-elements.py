from collections import Counter
class Solution(object):
    def countElements(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ccd = Counter(nums)
        nums.sort()
        p = Counter(nums).get(nums[0])
        e = Counter(nums).get(nums[-1])
        if len(ccd) == 1:
            return 0
        return len(nums) - p-e