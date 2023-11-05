class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        ans=0
        for i in left:
            ans=max(i,ans)
        for i in right:
            ans=max(n-i,ans)
        return ans 