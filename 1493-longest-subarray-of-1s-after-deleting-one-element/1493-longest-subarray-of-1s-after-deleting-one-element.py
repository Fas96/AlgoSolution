class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        n = len(nums)
        defauldict = defaultdict(int)
        l = 0
        ans = 0
        for r in range(n):
            defauldict[nums[r]] += 1
            while defauldict[0] > 1:
                defauldict[nums[l]] -= 1
                l += 1
            ans = max(ans, r - l)
        return ans
        