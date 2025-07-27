class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        if nums == sorted(nums, reverse=True) or nums == sorted(nums):
            return 0

        hv, i = 0, 1  
        while i < n - 1:
            left = i - 1
            right = i + 1 
            #move left i until wedont have same value as current num
            while left >= 0 and nums[left] == nums[i]:
                left -= 1
            if left < 0:
                i += 1
                continue 
            # Understand we move until no nums are same with right
            while right < n and nums[right] == nums[i]:
                right += 1
            if right >= n:
                i += 1
                continue
            #We check from left or right if we have hill or Valley
            if (nums[left] < nums[i] and nums[right] < nums[i]) or (nums[left] > nums[i] and nums[right] > nums[i]):
                hv += 1
                 
            i = right
        return hv