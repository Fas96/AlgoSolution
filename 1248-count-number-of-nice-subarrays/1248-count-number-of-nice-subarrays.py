class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        
        pref=list(accumulate([0 if num&1==0 else 1 for num in nums]))
        mp=defaultdict(int)
        res=0
        mp[0]=1
        for num in pref:
            if num-k in mp:
                res+=mp[num-k]
            mp[num]+=1
        return res
                
                
            