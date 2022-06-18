class Solution(object):
    def minTimeToType(self, word): 
        cur='a'
        tocount=0
        for ch in word:
            tocount+=1
            idx=abs(ord(ch)-ord(cur))
            tocount+=min(idx,26-idx)
            cur=ch
        return tocount