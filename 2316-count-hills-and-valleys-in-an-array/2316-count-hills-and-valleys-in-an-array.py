class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        if nums == sorted(nums, reverse=True) or nums == sorted(nums):
            return 0

        hv, i = 0, 1  # Start from 1 to compare with previous
        while i < n - 1:
            left = i - 1
            right = i + 1 
            while left >= 0 and nums[left] == nums[i]:
                left -= 1
            if left < 0:
                i += 1
                continue 
            while right < n and nums[right] == nums[i]:
                right += 1
            if right >= n:
                i += 1
                continue
            if (nums[left] < nums[i] and nums[right] < nums[i]) or \
               (nums[left] > nums[i] and nums[right] > nums[i]):
                hv += 1
                 
            i = right
            
        return hv