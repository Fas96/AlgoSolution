from collections import Counter

class Solution(object):
    def maxFrequency(self, nums, k, numOperations):
        """
        :type nums: List[int]
        :type k: int
        :type numOperations: int
        :rtype: int
        """
        nums.sort()
        n = len(nums)
        r = i = j = 0
        h = Counter()
        
        # Strategy 1: Target existing values
        for a in nums:
            # Expand j to include all reachable values
            while j < n and nums[j] <= a + k:
                h[nums[j]] += 1
                j += 1
            
            # Contract i to exclude unreachable values
            while i < n and nums[i] < a - k:
                h[nums[i]] += 1
                i += 1
            
            # Calculate max frequency for target value 'a'
            c = min(j - i, h[a] + numOperations)
            r = max(r, c)
        
        # Strategy 2: Target gap values
        i = 0
        for j in range(n):
            # Find window where all can converge
            while nums[i] + k + k < nums[j]:
                i += 1
            r = max(r, min(j - i + 1, numOperations))
        
        return r