class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n=len(values)
        maxIScore,score=0,0
        for i,x in enumerate(values):
            score=max(score,maxIScore+x-i)
            maxIScore=max(maxIScore,x+i)
        return score