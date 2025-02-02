class Solution:
    def checkString(self, s: str) -> bool:
        if 'a' not in s: return True
        aI=[]
        bI=[]
        for i in range(len(s)):
            if s[i]=='a':
                aI.append(i)
            else:
                bI.append(i)
        for v in aI:
            for u in bI:
                if v>u: return False
        return True

        