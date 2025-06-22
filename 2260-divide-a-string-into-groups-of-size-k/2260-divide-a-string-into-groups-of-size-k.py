class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n=len(s)
        ans=[]
        for i in range(0,n,k):
            f=s[i:i+k]
            if len(f)<k:
                f+=((k-len(f))*fill)
            ans.append(f)
        return ans
        