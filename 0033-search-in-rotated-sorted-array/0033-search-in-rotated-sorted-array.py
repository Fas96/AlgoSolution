class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        r=len(nums)-1
        mid =(l+r)//2
        while l<=r:
            if nums[l]==target:
                return l
            elif nums[r]==target:
                return r
            l+=1
            r-=1
        return -1
                
                
        