class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        dd = defaultdict(int)
        l = 0
        ans = 0
        for r in range(n):
            dd[nums[r]] += 1
            print(dd)
            while dd[0] > 1:
                dd[nums[l]] -= 1
                l += 1
            ans = max(ans, r - l)
        return ans
        