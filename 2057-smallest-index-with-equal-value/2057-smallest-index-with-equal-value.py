class Solution(object):
    def smallestEqual(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lsIndex = []

        for i in range(len(nums)):
            if i % 10 == nums[i]:
                lsIndex.append(i)
        return min(lsIndex) if len(lsIndex)>0 else -1