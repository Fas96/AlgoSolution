class Codec:
    def encode(self, strs: List[str]) -> str:
        ans=""
        for x in strs:
            ans+=(str(len(x))+"*#"+x)
        return ans
        
        

    def decode(self, s: str) -> List[str]:
        ans,n,i=[],len(s),0
        while i<n:
            j=i
            while s[j]!='*':
                j+=1
            l=int(str(s[i:j]))
            ans.append(s[j+2:j+2+l])
            i=j+2+l
        return ans
        


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))