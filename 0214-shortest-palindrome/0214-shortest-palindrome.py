class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if s==s[::-1]: return s
        tme=s[::-1] 
        for i in range(len(tme)):
            if s.startswith(tme[i:]):return tme[:i]+s
        return tme+s
        