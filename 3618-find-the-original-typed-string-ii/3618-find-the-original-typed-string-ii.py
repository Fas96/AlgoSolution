class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        m=10**9+7
        ans=1
        freq=[]
        st=word[0]
        ct=0
        for i in range(len(word)):
            if word[i]==st:
                ct+=1
            else:
                freq.append(ct)
                ct=1
                st=word[i]
        freq.append(ct)
        ans=1
        for i in freq:
            ans*=i
            ans=ans%m
        if len(freq)>=k:
            return ans
        #print(freq)
        dp=[1]+[0]* (k-1)
        prefix=[1]*k
        for i in freq:
            cudp=[0]*(k)
            for j in range(1,k):
                cudp[j]=prefix[j-1]
                if j-i>0:
                    cudp[j]=(cudp[j]-prefix[j-i-1])%m

            nprefix=[0]*k
            for j in range(1,k):
                nprefix[j]=(nprefix[j-1]+cudp[j])%m
            dp=cudp
            prefix=nprefix
            #print(prefix)
        return (ans-prefix[k-1])%m
