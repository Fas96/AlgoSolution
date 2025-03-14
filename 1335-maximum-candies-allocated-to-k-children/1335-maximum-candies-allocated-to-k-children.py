class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        sm=sum(candies)
        if(sm<k):return 0
        l,r=1,sm
        ans=0
        while l<=r:
            m=(l+r)//2
            c = sum(c//m for c in candies)
            if c>=k:
                ans=m
                l=m+1
            else:
                r=m-1

        return ans
        