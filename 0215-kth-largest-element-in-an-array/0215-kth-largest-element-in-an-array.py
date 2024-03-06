class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = nums[:k]
        heapq.heapify(n) 
        for num in nums[k:]:
            if num > n[0]:
                heapq.heappushpop(n, num)
        
        return n[0]
            
        