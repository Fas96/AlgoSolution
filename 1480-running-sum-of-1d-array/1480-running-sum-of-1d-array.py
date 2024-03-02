class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        N=len(nums)
        ans=[0]*N
        s=0
        for x,i in enumerate(nums):
            s+=i
            ans[x]=s
        return ans
            
        