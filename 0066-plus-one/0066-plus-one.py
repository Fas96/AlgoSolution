class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        def toSre(s):
            return str(s)
        s="".join(map(toSre,digits))
        sm=int(s)+1
        def digitss(v):
            an=[]
            while v>0:
                r=v%10
                v//=10
                an.append(r)
            return an
        return digitss(sm)[::-1]
        