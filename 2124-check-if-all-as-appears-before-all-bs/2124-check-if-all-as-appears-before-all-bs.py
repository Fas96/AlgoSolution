class Solution(object):
    def checkString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        aR = []
        bR = []
        for i in range( len(s)):
            if s[i] == 'a':
                aR.append(i)
            elif s[i] == 'b':
                bR.append(i)
        for a in aR:
            for b in bR:
                if a > b:
                    return False
        return True