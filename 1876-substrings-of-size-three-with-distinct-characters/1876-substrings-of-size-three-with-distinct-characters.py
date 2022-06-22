class Solution(object):
    def countGoodSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s) + 1
        sub=[s[x:y] for x, y in combinations(range(length), r=2)]

        l3=[i for i in sub if len(i)==3 and len(set(i))==3]
        return len(l3)