class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        
        for i in range(2,n-1):
            bstr=bin(i)[2:]
            print(bstr)
            if bstr[::-1]!=bstr:
                return False
        return True
        