class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        min_heap = []
        score =0
        for i in range(len(nums)):
            heapq.heappush(min_heap, -nums[i]) 
        for i in range(k):
            val=heapq.heappop(min_heap) 
            heapq.heappush(min_heap, -ceil(val*(-1) / 3))
            score+=(-val)

        return score