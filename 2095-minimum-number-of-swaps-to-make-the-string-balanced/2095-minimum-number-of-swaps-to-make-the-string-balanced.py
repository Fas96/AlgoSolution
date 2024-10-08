class Solution:
    def minSwaps(self, s: str) -> int:
        bal=0
        mx=0
        for x in s:
            bal=bal+(1 if x=='[' else -1)
            if bal<0:
                mx=max(mx,-bal)
        return (mx+1)//2