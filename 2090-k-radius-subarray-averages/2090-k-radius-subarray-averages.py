class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
#         ans=[-1]*(len(nums))
        
#         if len(ans) > k:
#             for i in range(k,len(nums)-k): 
#                 ans[i]= math.floor(sum(nums[i:i+k+1]+nums[i-k:i])/(len(nums[i:i+k+1]+nums[i-k:i]))) 
        prefix = list(accumulate([0] + nums))
        def k_radius(i):
            if i - k < 0 or i + k >= len(nums):
                return -1
            return (prefix[i + k + 1] - prefix[i - k]) // (2 * k + 1)
        
        return [k_radius(i) for i in range(len(nums))] 
        