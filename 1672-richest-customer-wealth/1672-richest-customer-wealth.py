class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans=0
        for x in accounts:
            ans=max(ans,sum(x))
        return ans
        