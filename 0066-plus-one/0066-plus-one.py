class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def toStr(s):
            return str(s)
        s="".join(map(toStr,digits))
        sm=int(s)+1
        def getDigits(v):
            an=[]
            while v>0:
                r=v%10
                v//=10
                an.append(r)
            return an
        return getDigits(sm)[::-1]
        