class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        ans=sorted([[sqrt(w*w+l*l),l*w] for w,l in dimensions],key=lambda x: (x[0], x[1]))
         
        return  ans[-1][1]