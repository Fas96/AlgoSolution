class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n=len(cost)
        an=[0]*n
        an[0]=cost[0]
        an[1]=cost[1]
        for i in range(2,n):
            an[i]= cost[i] +  min(an[i-1],an[i-2])
        return min(an[n-1], an[n-2])
        