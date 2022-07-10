class Solution(object):
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        s=0
        ss=0
        for i in range(len(cost)-1,-1,-1):
            sss= cost[i]+min(s,ss)
            ss=s
            s=sss
        
        return min(s,ss)
        