class Solution(object):
    def maximumUnits(self, boxTypes, truckSize):
        """
        :type boxTypes: List[List[int]]
        :type truckSize: int
        :rtype: int
        """

        boxTypes.sort(key=lambda x: (-x[1]))

        ress = 0
        for b, n in boxTypes:
            print(b,n)
            boxes = min(b, truckSize)
            ress += (boxes * n)
            truckSize -= boxes
            if truckSize == 0: return ress
        return ress