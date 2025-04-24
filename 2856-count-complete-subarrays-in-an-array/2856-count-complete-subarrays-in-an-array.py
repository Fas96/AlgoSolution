class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        k=len(set(nums))
        def cnt(nums,k):
            f=Counter()
            ans,w=0,0
            for i,n in enumerate(nums):
                f[n]+=1
                while len(f)>k:
                    f[nums[w]]-=1
                    if f[nums[w]]==0:
                        del f[nums[w]]
                    w+=1 
                ans+=(i-w+1)
            return ans
        return cnt(nums,k)- cnt(nums,k-1)