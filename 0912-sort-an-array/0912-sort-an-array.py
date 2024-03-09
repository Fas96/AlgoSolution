class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        fq = Counter(nums)     
        mnNum, mxNum = min(nums),max(nums)
        ans = []
        for num in range(mnNum, mxNum + 1):
            if num in fq:
                ans.extend([num]*fq[num])
        return ans
        