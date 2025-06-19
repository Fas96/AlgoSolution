class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()

        startIndex,n=0,len(nums)
        ans=0
        while startIndex<n:
            endOfGroup=nums[startIndex]+k
            startIndex=bisect_right(nums,endOfGroup,startIndex)
            ans+=1
        return ans