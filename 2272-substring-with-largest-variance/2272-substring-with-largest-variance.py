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
                    xy=max(xy,0)
                ans=max(d,ans) 
        return ans
        
'''
BR
For each pair of chars (x, y),  We need two variables xy and d to record values of 'x-y' for "x>=y"
xy : current difference of x and y 
d : possible difference of x and y with "at least one y"
If we meet x, xy and d will increase 1
If we meet y, xy will decrease 1 and d will used to record current xy.
Note "x>=y" is needed, so we will be reset xy as 0 if xy < 0
'''