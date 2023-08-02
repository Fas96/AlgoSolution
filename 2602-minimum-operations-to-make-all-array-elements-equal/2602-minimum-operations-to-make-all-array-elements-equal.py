class Solution:
    def minOperations(self, nums: List[int], queries: List[int]) -> List[int]:
        #TLE
        # ans=[]
        # nums.sort()
        # for val in queries:
        #     temp = sum(abs(val - i) for i in nums)
        #     ans.append(temp)
        # return ans
        
        n = len(nums)
        nums.sort()
        acc = [0] + list(accumulate(nums,operator.add))
        ans = []
        
        for q in queries:
            pos = bisect_left(nums,q)
            ans.append( (q*(pos) - acc[pos]) + ((acc[-1]-acc[pos]) - (n-pos)*q) )
    
        return ans