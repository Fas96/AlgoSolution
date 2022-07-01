class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """
        pweight=boxTypes
        

        pweight.sort(key=lambda x: -( x[1]))
        print(pweight)
        res = 0
        for f, s in pweight:
            print(f, s)
            b = min(f, truckSize)
            res += (s * b)
            truckSize -= b
            if truckSize == 0: return res
        return res