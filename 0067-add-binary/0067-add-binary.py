class Solution:
    def addBinary(self, a: str, b: str) -> str:
        an=int(a,2)+int(b,2) 
        return str(bin(an))[2:]
        