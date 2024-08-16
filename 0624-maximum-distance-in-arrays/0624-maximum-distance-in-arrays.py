class Solution:
    def maxDistance(self, A: List[List[int]]) -> int:

        mn, mnI = min((v[0], i) for i, v in enumerate(A))
        mx, mxI = max((v[-1], i) for i, v in enumerate(A))
        
        if mnI != mxI:
            return mx - mn
        
        smn, smnI= min((v[0], i) for i, v in enumerate(A) if i != mnI)
        smx, smxI = max((v[-1], i) for i, v in enumerate(A) if i != mxI)
        
        return max(abs(mx - smn), abs(smx - mn))

