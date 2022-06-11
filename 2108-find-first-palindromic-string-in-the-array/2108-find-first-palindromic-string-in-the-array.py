class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        for s in words:
            if s==s[::-1]:
                return s
        return ""