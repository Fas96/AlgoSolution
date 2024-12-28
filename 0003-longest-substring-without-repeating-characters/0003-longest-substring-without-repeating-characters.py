class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        f=Counter()
        ans,w=0,0
        for i,n in enumerate(s):
            f[n]+=1
            while max(f.values())>1:
                f[s[w]]-=1
                if f[s[w]]==0:
                    del f[s[w]]
                w+=1  
            ans=max(ans,i-w+1)
        return ans