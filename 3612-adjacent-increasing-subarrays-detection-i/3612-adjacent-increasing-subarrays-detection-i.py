class Solution:
    def hasIncreasingSubarrays(self, nums: list[int], k: int) -> bool:
        prev, increaseCount = 0, 1

        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                increaseCount += 1
            else:
                prev = increaseCount
                increaseCount = 1

            if increaseCount // 2 >= k or prev // 2 >= k or min(prev, increaseCount) >= k:
                return True

        return False