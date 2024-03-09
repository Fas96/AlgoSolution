class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos,neg=[],[]
        for x in nums:
            if x>0:
                pos.append(x)
            if x<0:
                neg.append(x)
        pl,nl=len(pos),len(neg)
        
        ans=[]
        
        for i in range(max(pl,nl)):
            if i<pl:
                ans.append(pos[i])
            if i<nl:
                ans.append(neg[i])
        
        return ans
        