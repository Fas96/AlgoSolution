class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        m=float("-inf")
        ans=0 
        for v in nums:
            if v>0:
                ans+=1
            else:
                m=max(m,ans)
                ans=0
        m=max(m,ans)
        return m

        