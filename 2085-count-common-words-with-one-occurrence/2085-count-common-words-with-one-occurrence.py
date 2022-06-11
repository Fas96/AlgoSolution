class Solution(object):
    def countWords(self, words1, words2):
        """
        :type words1: List[str]
        :type words2: List[str]
        :rtype: int
        """
        a, b = Counter(words1), Counter(words2)
        result = 0
        for key, val in a.items():
            if 1 != val:
                continue
            if b[key] == 1: 
                result += 1
        return result