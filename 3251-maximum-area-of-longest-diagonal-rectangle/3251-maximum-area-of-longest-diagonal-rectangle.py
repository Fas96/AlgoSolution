class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        return  sorted([[sqrt(w*w+l*l),l*w] for w,l in dimensions],key=lambda x: (x[0], x[1]))[-1][1]