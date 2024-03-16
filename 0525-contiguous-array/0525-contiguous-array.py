class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ones=0
        zeros=0
        ans=0
        mp={0:-1}
        for i,x in enumerate(nums):
            if x == 1:ones+=1
            if x == 0:zeros+=1
            d=zeros-ones
            if d in mp:
                ans=max(ans,i-mp[d])
            else:
                mp[d]=i
                
        return ans
        