class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        h = []
     
        for i, x in enumerate(nums):
            heappush(h, (x, i))
         
        for _ in range(k):
            val, idx = heappop(h) 
            new_val = val * multiplier   
            heappush(h, (new_val, idx))  
        h.sort(key= lambda x:(x[1],[0])) 
        return [v[0] for v in h]
            