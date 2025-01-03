class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        ans,n=0,len(nums)
        ps=list(accumulate(nums,operator.add))
        total_sum = ps[-1]
        for i in range(n-1): 
            if ps[i]>=total_sum -ps[i]:
                ans+=1
        return ans

        