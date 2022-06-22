class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        az = "abcdefghijklmnopqrstuvwxyz"
        freq = Counter(az)
        for v in sentence:
            freq[v] += 1
        return all([v > 1 for v in freq.values()])