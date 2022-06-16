class Solution(object):
    def areNumbersAscending(self, s):
        """
        :type s: str
        :rtype: bool
        """
        strToken = s.split(' ')
        numTok = [int(n) for n in strToken if n.isdigit()]
        res = True 

        for n in range(1, len(numTok)):
            if numTok[n - 1] > numTok[n] or numTok[n - 1] == numTok[n]:
                res = False
                break
        return res