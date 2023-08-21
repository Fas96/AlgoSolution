class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s)<2:return False
         
        for i in range(len(s)): 
            if s[:i]*s.count(s[:i])==s:
                return True
        return False