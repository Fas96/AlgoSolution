class Solution:
    def findMin(self, nums: List[int]) -> int:
        L,R=0,len(nums)-1
        res=nums[0]
        
        while L<=R:
            if nums[L] < nums[R]:
                return min(res,nums[L])
            pivot=L + ((R-L)//2)
            res = min(res,nums[pivot])
            if nums[pivot] >= nums[L]:
                L=pivot+1
            else:
                R=pivot-1
        return res
            
        