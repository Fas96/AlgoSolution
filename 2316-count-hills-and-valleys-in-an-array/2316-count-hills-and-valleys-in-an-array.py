class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        n = len(nums)
        if nums == sorted(nums, reverse=True) or nums == sorted(nums) or n < 3:
            return 0
            
        hillOrValley = 0
        idx = 1  
        while idx < n - 1:
            left = idx - 1
            right = idx + 1
             
            while left >= 0 and nums[left] == nums[idx]:
                left -= 1
            if left < 0:   
                idx += 1
                continue
                 
            while right < n and nums[right] == nums[idx]:
                right += 1
            if right >= n:   
                idx += 1
                continue
                 
            if (nums[left] < nums[idx] and nums[idx] > nums[right]) or (nums[left] > nums[idx] and nums[idx] < nums[right]):
                hillOrValley += 1
                 
            idx = right if right > idx + 1 else idx + 1
            
        return hillOrValley