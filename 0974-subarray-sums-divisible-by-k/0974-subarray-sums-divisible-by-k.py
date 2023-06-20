class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        ps,hm,ans=list(accumulate([0]+nums)),{},0 
        for subnum in ps:
            if subnum%k in hm:
                ans+=hm[subnum%k]
                hm[subnum%k]+=1
            else:
                hm[subnum%k]=1
                
        return ans
        