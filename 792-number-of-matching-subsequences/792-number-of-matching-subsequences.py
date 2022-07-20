class Solution(object):
    def numMatchingSubseq(self, s, words):   
        idx = defaultdict(list)
        for i, c in enumerate(s):
            idx[c].append(i)
        
        def isseq(w):
            prev = -1
            for c in w:
                prev = bisect_left(idx[c], prev)
                if prev == len(idx[c]):
                    return False
                prev = idx[c][prev] + 1
            return True
            
        return sum( c if isseq(w) else 0  for w, c in Counter(words).items())
        