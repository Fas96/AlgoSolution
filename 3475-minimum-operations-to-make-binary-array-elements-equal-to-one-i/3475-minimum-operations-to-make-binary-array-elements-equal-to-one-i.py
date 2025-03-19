class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans,i,ln=0,0,len(nums)
        for i in range(ln-2):
            if nums[i]==0:
                ans+=1 
                for j in range(i,i+3):
                    if nums[j]==0:
                        nums[j]=1
                    else:
                        nums[j]=0 
        
        return -1 if 0 in nums[ln-2:] else ans
        