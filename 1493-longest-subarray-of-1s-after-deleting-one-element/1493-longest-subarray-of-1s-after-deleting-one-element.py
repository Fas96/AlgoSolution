class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        ans = 0
        count = 0
        for r in range(n):
            if nums[r] == 0:
                count += 1
            while count > 1:
                if nums[l] == 0:
                    count -= 1
                l += 1
            ans = max(ans, r - l)
        return ans
        