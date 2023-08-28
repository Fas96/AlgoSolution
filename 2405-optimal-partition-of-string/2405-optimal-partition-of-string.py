class Solution:
    def partitionString(self, s: str) -> int:
        cnt=1
        inV=set()
        for c in s:
            if c not in inV:
                inV.add(c)
                continue
            inV.clear()
            inV.add(c)
            cnt+=1
        
        return cnt
        