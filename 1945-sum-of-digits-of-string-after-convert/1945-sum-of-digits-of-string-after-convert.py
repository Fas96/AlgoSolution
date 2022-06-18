class Solution(object):
    def getLucky(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        
        dk = {chr(i): ord(chr(i)) - ord('a') + 1 for i in range(ord('a'), ord('z') + 1, 1)}
        d = defaultdict(lambda: 0)
        for a, v in dk.items():
            d[a] = v
        for i in range(10):
            d[str(i)] = i

        for t in range(k):
            ad = 0
            for c in s:
                if len(str(d[c])) > 1:
                    for ts in list(str(d[c])):
                        ad += int(ts)
                else:
                    ad += d[c]
            s = str(ad)

        return ad