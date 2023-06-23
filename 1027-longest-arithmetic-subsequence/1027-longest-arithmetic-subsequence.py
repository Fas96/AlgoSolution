class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        from collections import defaultdict
        res = 0
        # default to have at least 2 subsequence
        memo = defaultdict(lambda: defaultdict(lambda: 2))
        # O(n^2)
        for i in range(1, len(nums)):
            for j in range(i):
                diff = nums[i]-nums[j]
                if diff in memo[j]:
                    memo[i][diff] = memo[j][diff]+1
                res = max(res, memo[i][diff])
        return res
                
            
        