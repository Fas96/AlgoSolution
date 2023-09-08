class Solution:
    def makeSmallestPalindrome(self, s: str) -> str: 
        a=list(s)
        L,R=0,len(a)-1
        
        while L<R:
            if a[L]<a[R]:
                a[R]=a[L]
            elif a[L]>a[R]:
                a[L]=a[R]
            L+=1
            R-=1
        return ''.join(a)
                
            