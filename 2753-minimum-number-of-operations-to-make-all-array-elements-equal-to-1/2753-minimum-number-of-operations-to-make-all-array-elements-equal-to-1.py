class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        overall_gcd = reduce(gcd, nums)
        if overall_gcd != 1:
            return -1
        if 1 in nums:
            return n - nums.count(1)
        min_len = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i+1, n):
                g = gcd(g, nums[j])
                if g == 1:
                    min_len = min(min_len, j - i + 1)
        total_ops = (min_len - 1) + n - 1
        return total_ops