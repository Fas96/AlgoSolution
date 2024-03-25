class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        f=Counter(nums)
        return [k for k,v in f.items() if v>1]