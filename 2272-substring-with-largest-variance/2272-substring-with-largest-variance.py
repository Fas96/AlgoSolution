class Solution:
    def largestVariance(self, s: str) -> int:
        ans, freq,N = 0, Counter(s),len(s)
         
         
        for x, y in permutations(set(s), 2): 
            if freq[x]==1: 
                continue
            xy, d = 0,- N
            for c in s:
                if c==x:
                    xy += 1
                    d += 1
                elif c==y:
                    xy -= 1
                    d = xy 
                    if xy<0: 
                        xy = 0
                if ans<d:
                    ans = d
        return ans
        