class Solution:
    def maxSideLength(self, mat: list[list[int]], threshold: int) -> int:
        n, m = len(mat), len(mat[0])
        prefix = [[0] * (m + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prefix[i][j] = mat[i-1][j-1] + prefix[i-1][j] + prefix[i][j-1] - prefix[i-1][j-1]
        
        def getSum(x1, y1, x2, y2):
            return prefix[x2+1][y2+1] - prefix[x1][y2+1] - prefix[x2+1][y1] + prefix[x1][y1]

        low, high = 1, min(n, m)
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            found = False
            for i in range(n - mid + 1):
                for j in range(m - mid + 1):
                    if getSum(i, j, i + mid - 1, j + mid - 1) <= threshold:
                        found = True
                        break
                if found: break
            
            if found:
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans