class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr=[]
        for x in nums:
            heappush(arr, -x)
        val=-float('inf')
        for i in range(k):
            val=-heappop(arr)
            
        return val 

        