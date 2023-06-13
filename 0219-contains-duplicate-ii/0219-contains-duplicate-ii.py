class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hm = {}
        for idx, value in enumerate(nums):  
            if nums[idx] in hm and idx - hm[value] <= k:
                return True
            hm[value]=idx
        return False
        