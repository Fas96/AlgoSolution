class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        f=Counter(nums)
        mxVal=max(f.values())
        return sum([1 if f[x]==mxVal else 0 for x in nums ])
        