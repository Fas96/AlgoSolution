class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hm = {}
        for i in range(len(nums)):
            if (target - nums[i]) in hm:
                return [i, hm.get(target - nums[i])]
            hm[nums[i]] = i
        return [-1,-1]