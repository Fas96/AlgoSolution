class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i in range(len(nums)):
            if (target - nums[i]) in hm:
                return [ hm.get(target - nums[i])+1,i+1]
            hm[nums[i]] = i
        return [-1,-1]