class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        ans, max_num, cnt = 0, 0, 0
        for i, num in enumerate(nums):
            if num > max_num:
                max_num = num
                ans, cnt = 1, 1
            elif num == max_num:
                cnt += 1
                ans = max(cnt, ans)
            else:
                cnt = 0
        return ans