class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        current_sum, count = 0, 0

        for right in range(len(nums)):
            current_sum += nums[right]

            while  current_sum * (right - left + 1) >= k:
                current_sum -= nums[left]
                left += 1
            
            count += right - left + 1

        return count
