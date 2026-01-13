class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        y_coor = []
        total_area = 0.0

        for x, y, d in squares:
            y_coor.append((y, d))
            total_area += d * d

        y_coor.sort()

        l = 0.0
        r = max(y + d for y, d in y_coor)
        target = total_area / 2.0
        eps = 1e-6

        while l <= r:
            m = (l + r) / 2.0
            curr = 0.0

            for y, d in y_coor:
                if y < m < y + d:
                    curr += d * (m - y)
                elif y + d <= m:
                    curr += d * d

            if curr >= target:
                r = m - 1e-6
            else:
                l = m + 1e-6

        return l