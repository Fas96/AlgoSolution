class Solution:
    def minOperations(self, nums: List[int]) -> int:
        c,i,ln=0,0,len(nums)
        while i<ln-2:

            if nums[i]==0:
                c=c+1

                for j in range(i,i+3):
                    if nums[j]==0:
                        nums[j]=1
                    else:
                        nums[j]=0
            i+=1
        if 0 in nums[ln-2:]:
            return -1
        
        return c
        