class Solution:
    def findDiagonalOrder(self, n: List[List[int]]) -> List[int]:
        return map(list.pop,sorted([i+j,j,t]for i,r in enumerate(n)for j,t in enumerate(r)))