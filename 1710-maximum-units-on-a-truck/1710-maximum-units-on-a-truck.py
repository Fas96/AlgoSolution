class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        pweight=boxTypes
        
        pweight.sort(key=lambda x:-x[1])
         
        res = 0
        for b, n in pweight:
            bb = min(b, truckSize)
            res += (bb * n)
            truckSize -= bb
            if truckSize == 0: return res
        return res