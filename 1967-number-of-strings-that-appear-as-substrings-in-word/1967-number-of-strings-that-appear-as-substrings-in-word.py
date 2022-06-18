class Solution(object):
    def numOfStrings(self, patterns, word):
        """
        :type patterns: List[str]
        :type word: str
        :rtype: int
        """

        def subseq(w):
            l = len(w) + 1
            return [w[x:y] for x, y in combinations(range(l), r=2)]

        ls = subseq(word)
        cnt = 0
        for p in patterns:
            if p in ls:
                cnt += 1
        return cnt
        