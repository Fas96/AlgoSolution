class Solution(object):
    def generate(self, numRows):
        res=[]
        dp=[1]
        res.append(dp)
        for _ in range(numRows-1):
            dp=[x+y for x, y in zip(dp+[0],[0]+dp)]
            res.append(dp)
        return res
        