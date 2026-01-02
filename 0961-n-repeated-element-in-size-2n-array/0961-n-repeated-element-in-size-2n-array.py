class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n=len(nums)//2
        f=Counter(nums)
        for k,v in f.items():
            if v==n:
                return k
        return -1
        