class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        maxi = 0
        total = 0
        i, j = 0, 0
        while j < len(nums):
            total += nums[j]
            while nums[j] * (j - i + 1) > total + k:
                total -= nums[i]
                i += 1
            maxi = max(maxi, j - i + 1)
            j += 1
        return maxi