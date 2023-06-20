class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans=[-1]*(len(nums))
        prefix=list(accumulate([0] + nums))
        
        if len(ans) > k:
            for i in range(k,len(nums)-k): 
                ans[i]= (prefix[i + k + 1] - prefix[i - k]) // (2 * k + 1) 
        return  ans
        