class Solution:
    def getLucky(self, s: str, k: int) -> int:
        nSVal=""
        for c in s:
            nSVal+=str(ord(c)-ord('a')+1)
        print(nSVal)
        while k:
            temp=0
            for c in nSVal:
                temp+=int(c)
            nSVal=str(temp)
            k-=1
        return int(nSVal)
        