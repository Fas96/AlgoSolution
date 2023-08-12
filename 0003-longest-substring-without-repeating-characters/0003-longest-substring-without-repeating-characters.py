class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        mp=defaultdict(int)
        j=ans=0
        
        for i in range(len(s)):
            mp[s[i]]+=1
            while mp[s[i]] > 1:
                mp[s[j]]-=1
                j+=1
            ans=max(ans,i-j+1) 
        return ans
        