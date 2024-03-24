class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        
        
        h = []
        count = Counter()
        res = []
        for i, f in zip(nums, freq):
            count[i] += f
            heappush(h, [-count[i], i])
            while h and count[h[0][1]] != -h[0][0]:
                heappop(h)
            res.append(-h[0][0] if h else 0)
        return res

#         ff=defaultdict(int)
#         ans=[]
#         mx=float("-inf")
#         for u,v in zip(nums,freq):
#             ff[u]+=v
            
#             if len(ff)>0:
#                 ans.append(max(ff.values()))
#             else:
#                 ans.append(0)
        
#         return ans

            