class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        print(''.join('%d:' % len(s) + s for s in strs))
        return ''.join('%d:' % len(s) + s for s in strs)
        

        
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """  
        i,n=0,len(s)
        ans=[]
        while i<n:
            j=s.find(':',i)
            i=j + 1 + int(s[i:j])
            ans.append(s[j+1:i])
        return  ans
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))