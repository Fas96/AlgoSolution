class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        hs=Counter(words)
        hq=[]
        heapq.heapify(hq)
        for kk,v in hs.items():
            heapq.heappush(hq,[-v,kk])
        ans=[]
        for i in range(k):
            ans.append(heapq.heappop(hq)[-1])
        return ans