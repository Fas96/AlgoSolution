class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num<=1:return True
        l,r=0,(2**31) - 1
        while l<=r:
            m=l+((r-l)//2)
            if m*m==num:
                return True
            if m*m>num:
                r=m-1
            else:
                l=m+1
        return False