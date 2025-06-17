class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen=set()
        for i,v in enumerate(nums):
            if v in seen:
                return True
            seen.add(v)
            if len(seen)>k:
                seen.remove(nums[i-k])
        return False
        