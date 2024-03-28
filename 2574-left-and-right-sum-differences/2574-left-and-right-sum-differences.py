class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        s=[]
        pf=list(accumulate([0]+nums[:-1]))
        rpf=list(accumulate(nums[::-1][0:]))[:-1][::-1]+[0]
        for i in range(min(len(pf),len(rpf))):
            s.append(abs(pf[i]-rpf[i]))
        return s
        