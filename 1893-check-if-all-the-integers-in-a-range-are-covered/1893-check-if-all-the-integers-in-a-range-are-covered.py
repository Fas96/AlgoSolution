class Solution(object):
    def isCovered(self, ranges, left, right):
        """
        :type ranges: List[List[int]]
        :type left: int
        :type right: int
        :rtype: bool
        """
        return all(any(l <= i <= r for l, r in ranges) for i in xrange(left, right + 1))