class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        sm,minAbs=0,inf
        negOdd=False
        for row in matrix:
            for x in row:
                minAbs=min(minAbs,abs(x))
                print(minAbs,negOdd)
                if x<0:
                    sm-=x
                    negOdd=1-negOdd
                else:
                    sm+=x
        return sm-2*minAbs*negOdd