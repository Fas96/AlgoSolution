class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums.sort()
        idx=[]
        for i in range(len(nums)):
            if target==nums[i]:
                idx.append(i)
       
        return idx