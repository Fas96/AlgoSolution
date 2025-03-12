class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        xx={1:0,-1:0}
        for x in nums:
            if x>0:
                xx[1]+=1
            elif x<0:
                xx[-1]+=1
        return max(xx[1],xx[-1])
        