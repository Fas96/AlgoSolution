class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        fstk=[]
        sstk=[]
        for x in s:
            if fstk and x=='#':
                fstk.pop()
            elif x!='#':
                fstk.append(x)
        for x in t:
            if sstk and x=='#':
                sstk.pop()
            elif x!='#':
                sstk.append(x)
        return fstk==sstk
                
                
        