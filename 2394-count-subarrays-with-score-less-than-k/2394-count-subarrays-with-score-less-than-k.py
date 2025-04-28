class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        left = 0
        sm, count = 0, 0

        for i,n in enumerate( nums):
            sm += n

            while  sm * (i - left + 1) >= k:
                sm -= nums[left]
                left += 1
            
            count += i - left + 1

        return count
