'''
*matrix decomposes it into separate lists each representing a row for example if matrix =[[1,2], [3, 4]] then *matrix returns two lists [1,2] and [3, 4]
zip([1, 2], [3, 4]) returns two lists of [1, 3] and [2, 4] which are the columns of the matrix
'''
class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows = {min(r) for r in matrix}

        cols = {max(c) for c in zip(*matrix)}
   
        return list(rows & cols)