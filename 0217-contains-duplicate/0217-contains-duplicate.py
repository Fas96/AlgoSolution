class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq=Counter(nums)
        vals=freq.values()
        for x in vals:
            if x>1: return True
        return False