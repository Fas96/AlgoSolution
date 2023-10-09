class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        d=Counter(nums)
        if target not in d:
            return [-1,-1]
        l,r=bisect_left(nums,target),bisect_right(nums,target)
        
        return [l,r-1]
        