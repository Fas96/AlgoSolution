class Solution:
    def finalString(self, s: str) -> str:
        ANS=[]
        for c in s:
            if c=='i':
                ANS=ANS[::-1]
            else: ANS.append(c)
        return "".join(ANS)
        