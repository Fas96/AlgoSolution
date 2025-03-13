class Solution:
    def is_valid(self, nums: List[int], que: List[List[int]], k: int) -> bool:
        n = len(nums)
        dist = [0] * n

        for i in range(k + 1):
            l, r, val = que[i]
            dist[l] += val
            if r + 1 < n:
                dist[r + 1] -= val

        cum_sum = 0
        for i in range(n):
            cum_sum += dist[i]
            dist[i] += cum_sum
            if nums[i] - cum_sum > 0:
                return False
        return True

    def minZeroArray(self, nums: List[int], que: List[List[int]]) -> int:
        n, q = len(nums), len(que)

        if all(x == 0 for x in nums):
            return 0  # No query required because all are already zero

        l, h, ans = 0, q - 1, -1
        while l <= h:
            mid = (l + h) // 2
            if self.is_valid(nums, que, mid):
                ans = mid + 1
                h = mid - 1
            else:
                l = mid + 1
        return ans