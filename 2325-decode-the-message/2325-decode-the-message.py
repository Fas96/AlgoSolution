class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        key=key.replace(' ','')
        mp={}
        cnt=0
        for i in range(len(key)):
            if  (len(key[i])!=' ') and key[i] not in mp:
                mp[key[i]]=chr(97+cnt)
                cnt+=1
    
        ans=''
        for c in message:
            if c in mp:
                ans+=mp[c]
            else:
                ans+=' '
        return ans
                
        