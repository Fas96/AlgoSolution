class Solution(object):
    def numDifferentIntegers(self, word):
        """
        :type word: str
        :rtype: int
        """
        for idx in range(len(word)):
            if word[idx].isalpha():
                word = word.replace(word[idx], " ")
        numList = set(word.split(" "))
        numList = [int(n) for n in numList if len(n) > 0]

        return len(set(numList))