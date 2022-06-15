class Solution(object):
    def countPoints(self, rings):
        """
        :type rings: str
        :rtype: int
        """
        
        h = {}
        for i in range(10):
            h[i] = list()
        for i in range(0, len(rings), 2):
            h[int(rings[i + 1])].append(rings[i])

        cnt = 0
        for k, v in h.items():
            if len(v) > 0:
                if 'R' in v and 'G' in v and 'B' in v:
                    cnt += 1
        return cnt
