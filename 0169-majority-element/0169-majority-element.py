class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        f=Counter(nums)
        mx=float('-inf')
        v=-1
        for x in set(nums):
            if f[x]>mx:
                mx=f[x]
                v=x
        return v
        