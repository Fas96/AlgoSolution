class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        return sum(y*(y-1)//2 for y in Counter(x%k for x in accumulate([0] + nums)).values())
        
#         pre=list(accumulate([0]+nums))
#         cnt,ans=[0]*k,0 
        
#         for x in pre:
#             ans+=cnt[x%k]
#             cnt[x%k]+=1
        # return ans
    
            
        
#         ps,hm,ans=list(accumulate([0]+nums)),{},0 
#         print([0 for _ in range(k)])
#         print([0]*k)
#         for subnum in ps:
#             if subnum%k in hm:
#                 ans+=hm[subnum%k]
#                 hm[subnum%k]+=1
#             else:
#                 hm[subnum%k]=1
        
#         return ans
        
    
    