class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f=Counter(nums)
        for k,v in f.items():
            if v>1:
                return k
        return -1
        