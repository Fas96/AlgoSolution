class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        freq = Counter(s)
        ls = list(freq.values())
        return len(set(ls))==1