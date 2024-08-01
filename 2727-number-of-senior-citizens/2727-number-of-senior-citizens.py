class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ans=0
        for x in details:
            if int(x[11:13])>60: ans+=1
        return ans
        