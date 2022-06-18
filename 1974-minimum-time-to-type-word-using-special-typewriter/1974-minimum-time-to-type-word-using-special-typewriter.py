class Solution(object):
    def minTimeToType(self, word): 
        cur='a'
        tocount=0
        for ch in word:
            tocount+=1
            tocount+=min(abs(ord(ch)-ord(cur)),26-abs(ord(ch)-ord(cur)))
            cur=ch
        return tocount