import heapq
from typing import List

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        
        # Pair each query with its original index, then sort them by value
        sorted_queries = [(val, idx) for idx, val in enumerate(queries)]
        sorted_queries.sort()

        result = [0] * len(queries)
        visited = set([(0, 0)])
        min_heap = [(grid[0][0], 0, 0)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        reachable_count = 0

        for query_value, original_index in sorted_queries:
            while min_heap and min_heap[0][0] < query_value:
                cell_value, row, col = heapq.heappop(min_heap)
                reachable_count += 1

                for dx, dy in directions:
                    new_row, new_col = row + dx, col + dy
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        if (new_row, new_col) not in visited:
                            visited.add((new_row, new_col))
                            heapq.heappush(min_heap, (grid[new_row][new_col], new_row, new_col))

            result[original_index] = reachable_count

        return result
        