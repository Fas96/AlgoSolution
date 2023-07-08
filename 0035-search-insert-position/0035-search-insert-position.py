class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        L,R=0,len(nums)
        
        while L<R:
            P=L+(R-L)//2
            print(nums[P])
            if nums[P]==target:
                return P
            if nums[P]<target:
                L=P+1
            else:
                R=P
        return R
                
        