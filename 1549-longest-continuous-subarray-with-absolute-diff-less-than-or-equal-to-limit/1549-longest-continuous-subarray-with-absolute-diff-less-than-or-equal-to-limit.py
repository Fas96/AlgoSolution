class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        n=len(nums)
        i=0
        ans=[]
        for j in range(n):
            bisect.insort(ans,nums[j])
            if ans[-1]-ans[0]>limit:
                ans.pop(bisect.bisect(ans,nums[i])-1)
                i+=1
        return j-i+1