class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n=len(values)
        maxIScore,ans=0,0
        for i,x in enumerate(values):
            ans=max(ans,maxIScore+x-i)
            maxIScore=max(maxIScore,x+i)
        return ans