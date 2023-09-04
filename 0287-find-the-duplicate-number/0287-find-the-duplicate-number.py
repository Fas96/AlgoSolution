class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for k,v in Counter(nums).items():
            if v>=2:
                return k 
        