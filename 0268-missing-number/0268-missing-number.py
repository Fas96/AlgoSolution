class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        l,r=0,len(nums)-1
        for i in range(max(nums)+1):
            i=bisect_left(nums,i)
            print(i)
            if i!=nums[i]:
                return i
        return nums[-1]+1
            