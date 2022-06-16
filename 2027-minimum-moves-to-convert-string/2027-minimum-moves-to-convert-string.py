class Solution(object):
    def minimumMoves(self, s):

        cnt = 0
        i=0
        while i <len(s):

            if s[i] == 'X':
                cnt += 1
                i += 3
            else:
                i += 1
        return cnt