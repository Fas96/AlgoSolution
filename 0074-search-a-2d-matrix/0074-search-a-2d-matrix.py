class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if len(matrix) == 0: return False
        if len(matrix[0]) == 0: return False
        m, n = len(matrix), len(matrix[0])
        l, r = 0, m * n - 1
        while l <= r: 
            # mid=l + ((r - l) //2)
            mid= (l + r) >> 1; 
            if matrix[mid // n][mid % n] == target:
                return True
            elif matrix[mid // n][mid % n] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False