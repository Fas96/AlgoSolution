class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool: 
        if len(matrix) == 0: return False
        if len(matrix[0]) == 0: return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0,  n - 1 
        while l<m and r>=0:
            if matrix[l][r] == target:
                return True
            elif matrix[l][r] > target:
                r-=1
            else:
                l+=1
        return False