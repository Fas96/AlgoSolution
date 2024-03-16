class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        sa=s1.split(" ")
        sb=s2.split(" ")
        k=(set(sa) ^ set(sb)) and (set(sb) ^ set(sa))
        ans=[]
        for x in k:
            if (x in sa) and sa.count(x)<2:
                ans.append(x)
            if (x in sb) and sb.count(x)<2:
                ans.append(x)
                
         
        return ans
        