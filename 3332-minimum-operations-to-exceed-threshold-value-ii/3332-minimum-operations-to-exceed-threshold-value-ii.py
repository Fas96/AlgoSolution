class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        pq = list(nums)
        heapq.heapify(pq)
        op = 0
        while len(pq) > 1:
            x = heapq.heappop(pq)
            y = heapq.heappop(pq)
            if x >= k:
                return op
            n = 2 * min(x, y) + max(x, y)
            heapq.heappush(pq, n)
            op += 1
        return op