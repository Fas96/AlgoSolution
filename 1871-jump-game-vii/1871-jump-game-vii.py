class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        ans=[0,1]
        for i in range(1,len(s)):
            ans.append(ans[-1]) 
            BEG= max(0,i- maxJump)
            END= max(0,i- minJump+1) 
            if  (ans[END]-ans[BEG]>0) and (s[i] == '0') :
                ans[-1]+=1
     
        return ans[-1]>ans[-2]
  