class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        def check(k):
            count = 0
            i = 0
            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= k:
                    i += 2
                    count += 1
                else:
                    i += 1
                if count >= p:
                    return True

            return count >= p

        l, r = 0, max(nums)
        while l < r:
            mid = l+((r - l) >> 1)
            if check(mid):
                r = mid
            else:
                l = mid + 1
        return l