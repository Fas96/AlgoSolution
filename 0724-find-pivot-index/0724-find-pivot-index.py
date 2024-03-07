class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        idx=-1
        f=list(accumulate(nums))
        b=list(accumulate(nums[::-1]))[::-1]
        for i in range(len(nums)):
            if f[i]==b[i]:
                return i
        return idx
        