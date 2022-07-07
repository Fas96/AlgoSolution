class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        f,ss,t=len(s1),len(s2),len(s3)
        if f+ss!=t:
            return False
        s,v=[(0,0)],set((0,0))
        while s:
            x,y=s.pop()
            if x+y==t:
                return True
            if x+1<=f and s1[x]==s3[x+y] and (x+1,y) not in v:
                s.append((x+1,y))
                v.add((x+1,y))
            if y+1<=ss and s2[y]==s3[x+y] and (x,y+1) not in v:
                s.append((x,y+1))
                v.add((x,y+1))
        
        return False