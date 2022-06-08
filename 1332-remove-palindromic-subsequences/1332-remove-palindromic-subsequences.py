class Solution(object):
    def removePalindromeSub(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)==0:
            return 0
        
        for i in range(len(s)//2):
            if s [ i ] != s[ len(s) - 1 - i]:
                return 2
            
        return 1
        