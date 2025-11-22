class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        ans = 0
        for x in nums:
            if x % 3 == 0:
                continue
            ans += min(x % 3, 3 - (x % 3))
        return ans