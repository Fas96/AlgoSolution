class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        ans=nums[k]
        MIN=nums[k]
        low=k
        high=k
        n=len(nums)
        while 0<=low-1 or high+1<n:

            if low==0 or high+1<n and nums[low-1]<nums[high+1]:
                high+=1
                MIN=min(MIN,nums[high])
            else:
                low-=1
                MIN=min(MIN ,nums[low])     
            ans=max(ans,MIN*(high-low+1))
        return ans 