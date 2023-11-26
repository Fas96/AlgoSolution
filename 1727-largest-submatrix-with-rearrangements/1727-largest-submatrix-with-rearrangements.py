class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        def prefix_sum(row_s, row):
            return list(map(lambda s, n: (s+n)*n, row_s, row))
        return max(max(map(mul, sorted(row, reverse = True), count(1))) for row in accumulate(matrix, prefix_sum))
        