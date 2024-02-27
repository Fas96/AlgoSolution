class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 : return False
        x,y=str(x),str(x)[::-1]
        return x==y
        