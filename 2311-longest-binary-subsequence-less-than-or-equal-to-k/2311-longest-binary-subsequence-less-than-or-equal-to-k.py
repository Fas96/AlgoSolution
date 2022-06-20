class Solution(object):
    def longestSubsequence(self, s, k):
        n=int(s,2)
        while n>k:
            for i in range(len(s)):
                if s[i]=='1':
                    s=s[:i]+s[i+1:]
                    break
            n=int(s,2)
            
        return len(s)