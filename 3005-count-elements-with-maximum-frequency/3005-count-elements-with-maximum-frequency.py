class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        f=Counter(nums)
        mxVal=max(f.values())
        cnt=0
        for x in nums:
            if f[x]==mxVal:
                cnt+=1
        return cnt
        