class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        dp = [1]
        for _ in range(rowIndex): 
            dp = [x + y for x, y in zip(dp+[0],   [0]+dp)]
        return dp