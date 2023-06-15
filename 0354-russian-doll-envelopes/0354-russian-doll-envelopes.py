class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        dp=[] 
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        for _,n in envelopes:
            idx=bisect.bisect_left(dp,n)
            if idx < len(dp):
                dp[idx]=n
            else:
                dp.append(n)
        return len(dp)
        