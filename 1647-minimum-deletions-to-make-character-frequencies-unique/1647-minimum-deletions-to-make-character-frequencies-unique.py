class Solution(object):
    def minDeletions(self, s):
        freq = sorted(list(Counter(s).values()), reverse=True)
        ttDel = 0
        nxFreq = len(s)
        for f in freq:
            nxFreq = min(nxFreq, f)
            ttDel += f - nxFreq
            if nxFreq > 0:
                nxFreq -= 1
        return ttDel