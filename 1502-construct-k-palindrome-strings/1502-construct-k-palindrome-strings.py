class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        f=Counter(s)
        ones=0
        for c in f.values():
            if c%2==1:
                ones+=1
        return ones<=k and k<=len(s)
        