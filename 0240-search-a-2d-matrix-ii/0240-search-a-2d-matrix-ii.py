class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m,n=len(matrix),len(matrix[0])
        l,r=0,n-1
        while l<m and r>=0:
            if matrix[l][r]==target:
                return True
            if matrix[l][r]>target:
                r-=1
            else:
                l+=1
        return False
        