class Solution(object):
    def divideString(self, s, k, fill):
        """
        :type s: str
        :type k: int
        :type fill: str
        :rtype: List[str]
        """
        rs = [s[i:i + k] for i in range(0, len(s), k)]
        if len(rs[-1]) != k:
            st = fill * (k - len(rs[-1]))
            rs[-1] += st
        return rs
        