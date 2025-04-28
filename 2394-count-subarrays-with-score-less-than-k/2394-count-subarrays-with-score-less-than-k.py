class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        current_sum, count = 0, 0

        for i,n in enumerate( nums):
            current_sum += n

            while  current_sum * (i - left + 1) >= k:
                current_sum -= nums[left]
                left += 1
            
            count += i - left + 1

        return count
