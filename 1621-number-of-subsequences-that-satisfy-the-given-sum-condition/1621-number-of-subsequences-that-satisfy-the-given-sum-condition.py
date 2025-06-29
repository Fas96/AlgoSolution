class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        MOD=10**9+7
        n=len(nums)
        left,right=0,n-1
        nums.sort()
        ans=0
        while left<=right:
            if nums[left]+nums[right]<=target:
                ans+=((1<<(right-left)))
                if ans>=MOD:
                    ans%=MOD
                left+=1
            else:
                right=bisect_right(nums,target-nums[left],lo=left,hi=right)-1
        return ans