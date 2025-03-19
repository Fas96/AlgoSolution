class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans,i,ln=0,0,len(nums)
        for i in range(ln-2):
            if nums[i]==0:
                ans+=1
                nums[i] ^= 1
                nums[i + 1] ^= 1
                nums[i + 2] ^= 1
        
        return -1 if 0 in nums[ln-2:] else ans
        