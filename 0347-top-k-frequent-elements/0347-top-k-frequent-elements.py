class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hs=Counter(nums)
        hq=[]
        heapq.heapify(hq)
        for kk,v in hs.items():
            heapq.heappush(hq,[-v,kk])
        ans=[]
        for i in range(k):
            ans.append(heapq.heappop(hq)[-1])
        return ans
            
            
        
        