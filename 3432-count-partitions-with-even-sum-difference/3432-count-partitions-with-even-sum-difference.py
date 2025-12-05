class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return sum([1 if ((sum(nums[:x])-sum(nums[x:]))%2==0) else 0 for x in range(1,len(nums))])
        