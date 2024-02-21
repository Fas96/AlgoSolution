class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans=0
        while left<right:
            left=left>>1
            right=right>>1
            ans+=1
        return left<<ans    