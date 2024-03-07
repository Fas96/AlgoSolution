class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        idx=-1
        f=accumulate(nums)
        b=accumulate(nums[::-1])
        f=list(f)
        b=list(b)[::-1]
        for i in range(len(nums)):
            if f[i]==b[i]:
                return i
        return idx
        