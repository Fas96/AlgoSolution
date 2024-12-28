class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        f=Counter()
        ans,start=0,0
        for i,n in enumerate(s):
            f[n]+=1
            while max(f.values())>1:
                f[s[start]]-=1
                if f[s[start]]==0:
                    del f[s[start]]
                start+=1  
            ans=max(ans,i-start+1)
        return ans