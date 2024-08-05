class Codec:
    def encode(self, strs: List[str]) -> str: 
        return ''.join('%d:' % len(s) + s for s in strs)
        

        
        

    def decode(self, s: str) -> List[str]: 
        i,n=0,len(s)
        ans=[]
        while i<n:
            j=s.find(':',i)
            i=j + 1 + int(s[i:j])
            ans.append(s[j+1:i])
        return  ans 