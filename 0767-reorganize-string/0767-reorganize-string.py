class Solution(object):
    def reorganizeString(self, s):
        a = sorted(sorted(s), key=s.count)
        h = len(a) / 2
        a[1::2], a[::2] = a[:int(h)], a[int(h):]
        return ''.join(a) * (a[-1:] != a[-2:-1])
        
        
        