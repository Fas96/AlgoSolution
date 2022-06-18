class Solution(object):
    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        for x in [list(b) for a, b in groupby(s)]:
            if len(x) < 2:
                res += x
            else:
                res += x[0:2]

        return ''.join(res)
            
        