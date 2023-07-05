class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        dd = {1:numOnes,0:numZeros,-1:numNegOnes} 
        res = 0
        for i in range(k):
            if dd[1] > 0:
                res += 1
                dd[1] -= 1
            elif dd[0] > 0:
                dd[0] -= 1
            elif dd[-1] > 0:
                res -= 1
                dd[-1] -= 1
            else:
                break
        return res
        