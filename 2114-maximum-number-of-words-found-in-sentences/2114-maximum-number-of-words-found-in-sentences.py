class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        m = 0
        for s in sentences:
            m = max(m, len(list(s.split(" "))))
        return m