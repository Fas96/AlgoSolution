class Solution:
    def vowelStrings(self, words: List[str], q: List[List[int]]) -> List[int]:
        ans=[]
        vw="aeiou"
        prefix = [1 if (w[0] in vw and w[-1] in vw) else 0 for w in words]
        ac=list(accumulate(prefix,operator.add))
        
        for x, y in q:
            if x == 0:
                ans.append(ac[y])
            else:
                ans.append(ac[y] - ac[x - 1])
        
        return ans