class Solution(object):
    def isPrefixString(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: bool
        """
        cmp=""
        for w in words:
            cmp+=w
            if cmp==s:
                return True
        return False