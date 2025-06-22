class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        n=len(s) 
        return [(s[i:i+k]+(k-len(s[i:i+k]))*fill) if (len(s[i:i+k])<k) else s[i:i+k] for i in range(0,n,k)]
        