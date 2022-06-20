class Solution(object):
    def countKDifference(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        cnt=0
        for i in range(len(nums)):
            for j in range(0, len(nums), 1):
                if j > i:
                    break
                if i == j:
                    continue
                if abs(nums[i] - nums[j]) == k:
                    cnt+=1 
        return cnt